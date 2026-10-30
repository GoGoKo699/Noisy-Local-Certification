# Noisy Local Certification

**How many copies are needed to recognize a fully known quantum state when every qubit produces one imperfect local report?**

For a Haar-typical pure target, fixed nonzero detector error makes even target-versus-maximally-mixed discrimination exponentially expensive. Knowing the target, choosing every measurement basis around it, using classical feedback across interleaved copies, and performing unlimited classical computation do not remove this cost.

If each independently reported bit flips with probability $0<q<1/2$, the optimal binary copy count at fixed error has rate

$$
N_{\mathrm{opt}}
=\bigl[(1-q)^2+q^2\bigr]^{-n+o(n)}.
$$

The acquisition model permits one destructive local projective measurement per input qubit. All accessed copies count. Repeated nondestructive readout, ancilla redundancy and coherent processing are additional resources, treated explicitly in the scientific account.

## Main results

| Question | Result |
|---|---|
| Can target knowledge and adaptive local bases avoid the binary cost? | A simultaneous product-effect bound and a complete-transcript hybrid argument give a converse for every allowed strategy, including interleaved copies. |
| Is the exponential rate attainable? | A fixed computational basis and a classical likelihood test attain it. The upper bound concerns sample complexity; classical computation can be exponential. |
| When can full fidelity certification use polynomially many copies? | For generic targets, exact-target certification at fixed tolerances has the noise budget $nq_n=O(\log n)$. Robust completeness has an explicit verifier-gap condition. |
| Does the binary theorem require an exponentially long preparation circuit? | A quantitative approximate-design transfer supplies polynomial-size circuit ensembles. This does not imply shallow circuits or efficient classical likelihood evaluation. |
| What changes if more quantum control is available? | Local redundancy, supplied inverse preparation and global acquisition measurements provide distinct, resource-accounted comparisons. |

Ideal local constant-copy certification and fixed-measurement noise suppression are established prior results. This account develops the optimum over target-informed adaptive measurements and its certification consequences. See [related work](references/RELATED_WORK.md) for the exact comparison and attribution.

## Read the science

Start with [the experiment, assumptions and theorem map](science/model-and-results.md). The [science index](science/README.md) connects the complete proofs, fidelity threshold, circuit-design extension and acquisition/control comparisons. The [reference list](references/REFERENCES.md) gives source versions and theorem locations.

## Reproduce the finite checks

With Python 3.12 and the pinned dependency installed:

```bash
python -m pip install -r requirements.txt
python code/verify.py
```

The [reproduction guide](code/README.md) explains the checks and the saved numerical report. They compare independently evaluated physical instruments, likelihood identities, Haar moments and the noise-inverted fidelity score. Universal probability and asymptotic claims are proved analytically.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
