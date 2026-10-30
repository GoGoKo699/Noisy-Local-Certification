# Reproduce the finite checks

From the repository root, use Python 3.12 with the pinned NumPy dependency:

```bash
python -m pip install -r requirements.txt
python code/verify.py
```

The command writes [results/verification.json](../results/verification.json), prints a compact summary and exits nonzero if a numerical identity or relative file link fails. The report records the actual runtime, fixed random seeds and hashes of the scientific source and checking code. Re-running it updates the observation time and may produce small floating-point differences across platforms.

## What is checked

| Check | Independent constructions compared | Scope |
|---|---|---|
| Haar chi-square moments | Direct bit-flip convolution of sampled Haar probabilities versus the exact mean and variance formulas | Ten cases with $n=2,4,6,8,10$ and $q=0.1,0.25$; Monte Carlo is a diagnostic, not a concentration proof |
| Adaptive noisy effects | Density-matrix measurement, noisy report and destructive partial trace versus the tensor-product leaf effect | Twelve trees, $n=2,3,4,5$, with outcome-dependent axes |
| Interleaved hybrids | Physical instruments on all input copies versus by-copy likelihood products and the sum of single-replacement relative entropies | Two and three copies of two-qubit targets, adaptive qubit order, interleaving and outcome-dependent stopping |
| Fidelity score inversion | Physical noisy POVM probabilities versus the classical bit-flip channel and its inverse-score expectation | All Pauli settings and outcomes for $n=2,3,4$ at four noise values |
| Ideal verification observable | Exact averaged score operator, conditional-state formula, target eigenspace and restricted spectral gap | Haar targets, zero-probability target branches and a generic product target with zero gap |
| Navigation | Relative Markdown file links versus the source tree | File destinations; actual hosted rendering is a separate inspection |

The two numerical modules can also be run independently:

```bash
python code/core_checks.py
python code/fidelity_checks.py
```

They print JSON without changing the scientific files. Floating-point checks use explicit tolerances appropriate to these small matrix calculations. The Monte Carlo check reports deviations in units of the exact standard error and has a broad six-standard-error diagnostic cutoff with a fixed seed. No large-system finite-size inference rests on that cutoff.

## Analytical claims and numerical limits

The uniform bound over all target-dependent measurement choices, the optimal asymptotic exponential rate, the full-fidelity polynomial threshold and the design-transfer guarantee are established by the scientific proofs. The finite checks cannot enumerate every protocol or certify those theorems experimentally. Likewise, small random-circuit simulations would not verify the required high-order design accuracy; no such inference is made.

The independent interleaving calculation is useful because a proof that only chains completed copies would leave a resource-model gap. It directly verifies the complete-transcript hybrid factorization on finite physical experiments with stopping. The fidelity checks exercise zero-probability conditional branches so that the implementation does not silently divide by zero or assume a positive verifier gap for every product target.
