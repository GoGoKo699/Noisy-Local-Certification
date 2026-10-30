"""Independent finite checks for the noisy local measurement model.

These calculations test exact identities and finite experiments. They do not
replace the uniform concentration proof or establish asymptotic typicality.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

SEED = 20261030135546
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULIS = (X, Y, Z)


def kron_all(matrices):
    result = np.ones((1, 1), dtype=complex)
    for matrix in matrices:
        result = np.kron(result, matrix)
    return result


def haar_state(rng, n):
    vector = rng.normal(size=2**n) + 1j * rng.normal(size=2**n)
    return vector / np.linalg.norm(vector)


def noisy_distribution(probabilities, n, q):
    values = probabilities.copy().reshape([2] * n)
    for axis in range(n):
        values = (1 - q) * values + q * np.flip(values, axis=axis)
    return values.reshape(-1)


def moment_checks(rng):
    cases = []
    for n, q in itertools.product((2, 4, 6, 8, 10), (0.1, 0.25)):
        repetitions = 4000 if n <= 6 else 2000
        d = 2**n
        s = 1 - 2 * q
        w = (1 + s * s) ** n - 1
        v = (1 + s**4) ** n - 1
        exact_mean = w / (d + 1)
        exact_variance = (
            2 * d * ((d + 1) * v + w * w)
            / ((d + 1) ** 2 * (d + 2) * (d + 3))
        )
        samples = []
        for _ in range(repetitions):
            psi = haar_state(rng, n)
            p = noisy_distribution(np.abs(psi) ** 2, n, q)
            samples.append(float(d * np.sum((p - 1 / d) ** 2)))
        mean = float(np.mean(samples))
        variance = float(np.var(samples, ddof=1))
        cases.append({
            "n": n, "q": q, "repetitions": repetitions,
            "exact_mean": exact_mean, "empirical_mean": mean,
            "mean_standard_errors": (mean - exact_mean)
            / math.sqrt(exact_variance / repetitions),
            "exact_variance": exact_variance,
            "empirical_variance": variance,
            "variance_ratio": variance / exact_variance,
        })
    # A reproducibility diagnostic, not an inferential proof of the formula.
    if max(abs(x["mean_standard_errors"]) for x in cases) > 6:
        raise AssertionError("Haar-moment Monte Carlo diagnostic exceeded six standard errors")
    return cases


def measure_and_discard(rho, site, observable, report, q):
    """Apply the physical noisy instrument, retaining no measured qubit."""
    remaining = int(round(math.log2(rho.shape[0])))
    others = [j for j in range(remaining) if j != site]
    order = [site] + others + [site + remaining] + [j + remaining for j in others]
    dim = 2 ** (remaining - 1)
    tensor = rho.reshape([2] * (2 * remaining)).transpose(order).reshape(2, dim, 2, dim)
    _, vectors = np.linalg.eigh(observable)
    output = np.zeros((dim, dim), dtype=complex)
    for true_bit in (0, 1):
        ket = vectors[:, 1 - true_bit]
        conditional = np.einsum("i,iajb,j->ab", ket.conj(), tensor, ket)
        output += ((1 - q) if report == true_bit else q) * conditional
    return output


def adaptive_effect_checks(rng):
    cases = []
    for n, q in itertools.product((2, 3, 4, 5), (0.07, 0.2, 0.4)):
        d = 2**n
        psi = haar_state(rng, n)
        rho = np.outer(psi, psi.conj())
        axes = {}
        for depth in range(n):
            for history in range(2**depth):
                r = rng.normal(size=3)
                axes[depth, history] = r / np.linalg.norm(r)
        instrument_values, effect_values = [], []
        for outcome in range(d):
            state, history = rho.copy(), 0
            factors = []
            for depth in range(n):
                bit = (outcome >> (n - 1 - depth)) & 1
                observable = sum(c * p for c, p in zip(axes[depth, history], PAULIS))
                state = measure_and_discard(state, 0, observable, bit, q)
                factors.append((I + (-1) ** bit * (1 - 2 * q) * observable) / 2)
                history = (history << 1) | bit
            instrument_values.append(float(np.trace(state).real))
            effect_values.append(float(np.vdot(psi, kron_all(factors) @ psi).real))
        discrepancy = float(np.max(np.abs(np.array(instrument_values) - effect_values)))
        if discrepancy > 1e-12 or abs(sum(instrument_values) - 1) > 1e-12:
            raise AssertionError("Adaptive noisy product-effect identity failed")
        cases.append({"n": n, "q": q, "maximum_probability_difference": discrepancy,
                      "total_probability": sum(instrument_values)})
    return cases


def interleaved_hybrid_check(rng, n, copies, q):
    """Compare full quantum instruments with the by-copy likelihood identity."""
    psi = haar_state(rng, n)
    target = np.outer(psi, psi.conj())
    mixed = np.eye(2**n) / 2**n
    labels = tuple((copy, site) for copy in range(copies) for site in range(n))
    models = [kron_all([target] * copies), kron_all([mixed] * copies)]
    for replaced in range(copies):
        models.append(kron_all([mixed if j == replaced else target for j in range(copies)]))
    leaf_probabilities = []
    leaf_ratios = []

    def recurse(states, unread, history, code, factors):
        # This outcome-dependent stopping rule exercises partial-copy records.
        if not unread or (len(history) >= 3 and code % 7 == 3):
            probabilities = np.array([np.trace(state).real for state in states])
            likelihoods = []
            for local in factors:
                effect = kron_all(local)
                denominator = np.trace(effect).real / (2**n)
                likelihoods.append(float(np.vdot(psi, effect @ psi).real / denominator))
            leaf_probabilities.append(probabilities)
            leaf_ratios.append(likelihoods)
            return
        # Select a copy cyclically, with history-dependent within-copy order.
        preferred = (len(history) + (code & 1)) % copies
        eligible = [j for j, label in enumerate(unread) if label[0] == preferred]
        site = eligible[code % len(eligible)] if eligible else code % len(unread)
        copy, original_site = unread[site]
        local_rng = np.random.default_rng(SEED + 173 * code + 11 * len(unread))
        direction = local_rng.normal(size=3)
        direction /= np.linalg.norm(direction)
        observable = sum(c * p for c, p in zip(direction, PAULIS))
        next_unread = unread[:site] + unread[site + 1:]
        for bit in (0, 1):
            updated = [measure_and_discard(state, site, observable, bit, q) for state in states]
            next_factors = [[f.copy() for f in local] for local in factors]
            next_factors[copy][original_site] = (I + (-1) ** bit * (1 - 2 * q) * observable) / 2
            recurse(updated, next_unread, history + (bit,), 2 * code + bit, next_factors)

    recurse(models, labels, (), 1, [[I.copy() for _ in range(n)] for _ in range(copies)])
    probabilities = np.stack(leaf_probabilities)
    ratios = np.stack(leaf_ratios)
    p, null = probabilities[:, 0], probabilities[:, 1]
    hybrids = probabilities[:, 2:]
    if np.any(probabilities <= 0):
        raise AssertionError("Unexpected zero probability in the positive-noise check")
    hybrid_ratio_error = float(np.max(np.abs(p[:, None] / hybrids - ratios)))
    product_ratio_error = float(np.max(np.abs(p / null - np.prod(ratios, axis=1))))
    total_kl = float(np.sum(p * np.log(p / null)))
    hybrid_kl = float(np.sum(p[:, None] * np.log(p[:, None] / hybrids)))
    normalization_error = float(np.max(np.abs(probabilities.sum(axis=0) - 1)))
    if max(hybrid_ratio_error, product_ratio_error, abs(total_kl - hybrid_kl), normalization_error) > 2e-11:
        raise AssertionError("Interleaved full-transcript hybrid identity failed")
    return {"n": n, "copies": copies, "q": q, "terminal_records": len(p),
            "hybrid_ratio_error": hybrid_ratio_error,
            "product_ratio_error": product_ratio_error,
            "direct_kl": total_kl, "sum_hybrid_kl": hybrid_kl,
            "kl_identity_error": abs(total_kl - hybrid_kl),
            "normalization_error": normalization_error}


def run_checks():
    rng = np.random.default_rng(SEED)
    moments = moment_checks(rng)
    adaptive = adaptive_effect_checks(rng)
    interleaved = [interleaved_hybrid_check(rng, 2, copies, q)
                   for copies, q in itertools.product((2, 3), (0.13, 0.31))]
    return {"status": "pass", "seed": SEED,
            "scope": "Finite identities and independent physical instruments; no asymptotic or novelty certificate.",
            "moments": moments, "adaptive": adaptive, "interleaved": interleaved,
            "max_mean_standard_errors": max(abs(x["mean_standard_errors"]) for x in moments),
            "maximum_adaptive_probability_error": max(x["maximum_probability_difference"] for x in adaptive),
            "maximum_interleaved_kl_error": max(x["kl_identity_error"] for x in interleaved)}


if __name__ == "__main__":
    import json
    print(json.dumps(run_checks(), indent=2))
