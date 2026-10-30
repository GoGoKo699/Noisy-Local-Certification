"""Deterministic checks for the fidelity-certification score.

Run with ``python code/fidelity_checks.py``.  Only NumPy and the Python
standard library are required.  ``run_checks()`` returns a JSON-serializable
report and raises AssertionError if a check fails.

The checks enumerate all Pauli basis patterns and all outcomes for two,
three, and four qubits.  They compare three independently assembled objects:
the conditional-state observable, its ideal score operator, and probabilities
from noisy local POVM effects.  Applying the inverse detector matrix to the
score must preserve the expectation under those noisy probabilities.

These finite checks validate the algebra and the zero-branch convention.
They do not establish asymptotic Haar typicality or replace the proofs.
"""

from itertools import product
import json
import sys

import numpy as np


SEED = 61030
SYSTEM_SIZES = (2, 3, 4)
NOISE_RATES = (0.0, 0.01, 0.15, 0.30)
ABS_TOL = 1e-10
KERNEL_TOL = 1e-9


def _tensor(factors):
    result = np.array([1.0], dtype=complex)
    for factor in factors:
        result = np.kron(result, factor)
    return result


def _basis_matrices():
    """Columns are outcome eigenvectors, in the order Z, X, Y."""
    return (
        np.eye(2, dtype=complex),
        np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2),
        np.array([[1, 1], [1j, -1j]], dtype=complex) / np.sqrt(2),
    )


def _target(kind, n, rng):
    dimension = 2**n
    if kind == "haar_draw":
        vector = rng.normal(size=dimension) + 1j * rng.normal(size=dimension)
        return vector / np.linalg.norm(vector)
    if kind == "zero_branch_product":
        vector = np.zeros(dimension, dtype=complex)
        vector[0] = 1.0
        return vector
    if kind == "nonzero_branch_product":
        local_states = [
            np.array([np.sqrt(0.3), np.exp(0.37j * (i + 1)) * np.sqrt(0.7)])
            for i in range(n)
        ]
        return _tensor(local_states)
    raise ValueError(f"Unknown target kind: {kind}")


def _conditional_observable(psi, n, bases):
    """Construct O directly from conditional target projectors on qubit 0."""
    dimension = 2**n
    target_matrix = psi.reshape(2, -1)
    observable = np.zeros((dimension, dimension), dtype=complex)
    table = {}
    zero_branches = 0
    positive_weights = []

    for theta_b in product(range(3), repeat=n - 1):
        entries = []
        for bits_b in product(range(2), repeat=n - 1):
            ket_b = _tensor([bases[t][:, bit] for t, bit in zip(theta_b, bits_b)])
            projected = target_matrix @ ket_b.conj()
            weight = float(np.vdot(projected, projected).real)
            if weight == 0.0:
                conditional = np.zeros((2, 2), dtype=complex)
                zero_branches += 1
            else:
                conditional = np.outer(projected, projected.conj()) / weight
                positive_weights.append(weight)
            entries.append(conditional)
            observable += (
                np.kron(conditional, np.outer(ket_b, ket_b.conj())) / 3 ** (n - 1)
            )
        table[theta_b] = entries

    return observable, table, zero_branches, min(positive_weights)


def _noise_matrices(n, q):
    forward = np.array([[1 - q, q], [q, 1 - q]], dtype=float)
    inverse = np.array([[1 - q, -q], [-q, 1 - q]], dtype=float) / (1 - 2 * q)
    return _tensor([forward] * n).real, _tensor([inverse] * n).real


def run_checks():
    """Return the finite-check report; raise AssertionError on a mismatch.

    Absolute tolerance 1e-10 is conservative for complex128 arithmetic on
    matrices of dimension at most 16.  The largest inverse-channel row norm
    used here is (1 - 2*0.30)^(-4) = 39.0625.  A separate 1e-9 eigenvalue
    threshold identifies exact kernels; positive tested gaps are far larger.
    """
    rng = np.random.default_rng(SEED)
    bases = _basis_matrices()
    max_errors = {}
    reports = []
    total_basis_patterns = 0
    total_noisy_basis_experiments = 0

    def check_close(label, actual, expected, tolerance=ABS_TOL):
        difference = np.asarray(actual) - np.asarray(expected)
        error = float(np.max(np.abs(difference)))
        if not np.isfinite(error) or error > tolerance:
            raise AssertionError(f"{label}: error {error:.6g} exceeds {tolerance:.6g}")
        max_errors[label] = max(max_errors.get(label, 0.0), error)

    def check(condition, message):
        if not bool(condition):
            raise AssertionError(message)

    for n in SYSTEM_SIZES:
        dimension = 2**n
        outcome_strings = tuple(product(range(2), repeat=n))
        noise = {q: _noise_matrices(n, q) for q in NOISE_RATES}

        for kind in ("haar_draw", "zero_branch_product", "nonzero_branch_product"):
            psi = _target(kind, n, rng)
            matrix = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(
                size=(dimension, dimension)
            )
            rho = matrix @ matrix.conj().T
            rho /= np.trace(rho)
            observable, conditional, zeros, min_weight = _conditional_observable(
                psi, n, bases
            )
            score_operator = np.zeros_like(observable)
            averaged_score = 0.0

            for theta in product(range(3), repeat=n):
                total_basis_patterns += 1
                basis = _tensor([bases[t] for t in theta])
                ideal_probabilities = np.diag(basis.conj().T @ rho @ basis).real
                scores = np.empty(dimension, dtype=float)
                local_projectors = [
                    [np.outer(bases[t][:, bit], bases[t][:, bit].conj()) for bit in (0, 1)]
                    for t in theta
                ]

                for index, bits in enumerate(outcome_strings):
                    conditional_state = conditional[theta[1:]][index % (2 ** (n - 1))]
                    shadow = 3 * local_projectors[0][bits[0]] - np.eye(2)
                    scores[index] = float(np.trace(conditional_state @ shadow).real)
                    projector = np.outer(basis[:, index], basis[:, index].conj())
                    score_operator += scores[index] * projector / 3**n

                check(np.min(scores) >= -1 - ABS_TOL, "Ideal score below -1")
                check(np.max(scores) <= 2 + ABS_TOL, "Ideal score above 2")
                ideal_mean = float(ideal_probabilities @ scores)
                averaged_score += ideal_mean / 3**n

                for q in NOISE_RATES:
                    total_noisy_basis_experiments += 1
                    forward, inverse = noise[q]
                    corrected = inverse @ scores
                    physical_noisy_probabilities = np.empty(dimension, dtype=float)

                    # Independent quantum construction: no use of the forward
                    # channel matrix when evaluating these noisy POVM effects.
                    for index, reported in enumerate(outcome_strings):
                        effects = [
                            (1 - q) * local_projectors[site][bit]
                            + q * local_projectors[site][1 - bit]
                            for site, bit in enumerate(reported)
                        ]
                        physical_noisy_probabilities[index] = float(
                            np.trace(rho @ _tensor(effects)).real
                        )

                    check_close(
                        "physical_vs_classical_noisy_probabilities",
                        physical_noisy_probabilities,
                        forward @ ideal_probabilities,
                    )
                    check_close(
                        "physical_noisy_probability_normalization",
                        physical_noisy_probabilities.sum(),
                        1.0,
                    )
                    check(
                        np.min(physical_noisy_probabilities) >= -ABS_TOL,
                        "A noisy POVM probability is negative",
                    )
                    check_close(
                        "inverse_score_unbiasedness",
                        physical_noisy_probabilities @ corrected,
                        ideal_mean,
                    )
                    check_close("channel_inverse_identity", forward @ inverse, np.eye(dimension))
                    bound = 1.5 * (1 - 2 * q) ** (-n)
                    check(
                        np.max(np.abs(corrected - 0.5)) <= bound + ABS_TOL,
                        "Corrected score exceeds the proved centered bound",
                    )

            check_close("score_operator_vs_conditional_observable", score_operator, observable)
            check_close("averaged_score_expectation", averaged_score, np.trace(rho @ observable).real)
            check_close("observable_hermiticity", observable, observable.conj().T)
            check_close("target_in_unit_eigenspace", observable @ psi, psi)

            spectrum = np.linalg.eigvalsh(observable)
            check(np.min(spectrum) >= -ABS_TOL, "Observable is not positive semidefinite")
            check(np.max(spectrum) <= 1 + ABS_TOL, "Observable exceeds the identity")
            h_spectrum = np.linalg.eigvalsh(np.eye(dimension) - observable)
            kernel_dimension = int(np.count_nonzero(np.abs(h_spectrum) <= KERNEL_TOL))
            gap_from_full_spectrum = float(h_spectrum[1])

            # Independently restrict O to psi-perpendicular, rather than
            # selecting its second eigenvalue by indexing the full spectrum.
            orthonormal, _ = np.linalg.qr(
                np.column_stack((psi, np.eye(dimension, dtype=complex))), mode="complete"
            )
            perpendicular = orthonormal[:, 1:]
            restricted = perpendicular.conj().T @ observable @ perpendicular
            gap_from_restriction = float(1 - np.linalg.eigvalsh(restricted)[-1])
            check_close("gap_restriction_vs_full_spectrum", gap_from_restriction, gap_from_full_spectrum)

            if kind == "haar_draw":
                check(zeros == 0, "Haar draw unexpectedly has an exact zero branch")
                check(kernel_dimension == 1, "Haar example has a degenerate unit eigenspace")
                check(gap_from_restriction > KERNEL_TOL, "Haar example gap is numerically zero")
            elif kind == "zero_branch_product":
                projector_zero = np.diag([1.0, 0.0])
                expected = _tensor(
                    [projector_zero] + [(2 * np.eye(2) + projector_zero) / 3] * (n - 1)
                )
                check(zeros > 0, "Zero-branch test did not exercise a zero branch")
                check_close("zero_branch_exact_observable", observable, expected)
                check_close("zero_branch_gap", gap_from_restriction, 1 / 3)
                check(kernel_dimension == 1, "Zero-branch product kernel has wrong dimension")
            else:
                ket_a = np.array([np.sqrt(0.3), np.exp(0.37j) * np.sqrt(0.7)])
                expected = np.kron(np.outer(ket_a, ket_a.conj()), np.eye(2 ** (n - 1)))
                check(zeros == 0, "Generic product test unexpectedly has a zero branch")
                check_close("nonzero_product_exact_observable", observable, expected)
                check_close("nonzero_product_gap", gap_from_restriction, 0.0)
                check(
                    kernel_dimension == 2 ** (n - 1),
                    "Generic product kernel has wrong dimension",
                )

            reports.append(
                {
                    "n": n,
                    "target": kind,
                    "zero_conditional_target_branches": zeros,
                    "minimum_positive_branch_weight": float(min_weight),
                    "gap": gap_from_restriction,
                    "kernel_dimension_of_identity_minus_observable": kernel_dimension,
                }
            )

    return {
        "passed": True,
        "seed": SEED,
        "arithmetic": "NumPy complex128 / float64",
        "absolute_tolerance": ABS_TOL,
        "kernel_eigenvalue_tolerance": KERNEL_TOL,
        "system_sizes": list(SYSTEM_SIZES),
        "noise_rates": list(NOISE_RATES),
        "target_cases": reports,
        "basis_patterns_enumerated": total_basis_patterns,
        "noisy_basis_experiments": total_noisy_basis_experiments,
        "maximum_absolute_errors": max_errors,
    }


if __name__ == "__main__":
    try:
        report = run_checks()
    except Exception as error:
        print(json.dumps({"passed": False, "error": str(error)}, indent=2))
        sys.exit(1)
    print(json.dumps(report, indent=2, sort_keys=True))
