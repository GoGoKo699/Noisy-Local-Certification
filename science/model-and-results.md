# Known targets and noisy local records

Knowing the desired quantum state can make certification much easier than tomography. Ideal local Pauli measurements can certify a Haar-typical pure target with a constant number of copies at fixed accuracy [Du et al.](../references/REFERENCES.md#du). This account asks how that capability changes when each local measurement produces one imperfect classical report.

The central result is an optimal exponential copy rate for a deliberately simple promise problem. The source is either the known pure target or the maximally mixed state. Even this distinction becomes exponentially expensive at fixed nonzero local reporting error, after optimizing measurement axes, classical feedback and all classical processing. A separate consequence identifies when full fidelity certification can retain polynomial copy complexity.

## 1. The experiment and its resources

The target is a pure state $`\psi=|\psi\rangle\langle\psi|`$ of $`n`$ qubits. Let $`d=2^n`$ and $`\tau=I/d`$. The verifier receives independent copies of one fixed source state. For the binary task the source is promised to be $`\psi`$ or $`\tau`$; for fidelity certification the alternative is any density operator satisfying the stated fidelity promise.

The complete target description and the exact detector parameter are supplied to the verifier. Classical storage, arithmetic and computation are unrestricted. In particular, the measurement strategy may be chosen after the target is known. This is an information-theoretic sample model: a short description, efficiently evaluable amplitudes or efficient classical likelihood computation is not assumed for Haar targets.

Each physical input qubit can receive at most one destructive binary projective measurement. The choice of its Bloch axis, the order of qubits and copies, and the decision to stop can depend on the target and all previously reported outcomes. Copies may be interleaved. The ideal measurement outcome $`x`$ is reported as $`y=x\oplus e`$, where $`e`$ is an independent Bernoulli variable with known probability $`q`$. Errors are independent across all sites and copies. Measurement bases and their classical labels are ideal.

The resource is a deterministic worst-case cap $`N`$ on copies accessed. All attempts count, including discarded or postselected records. Unused sites and copies may remain unread. Random choices are allowed; their seeds can be included in a refined classical transcript. The final decision may be any classical function of the transcript. No operation couples input qubits coherently, no quantum memory connects source copies, and no additional ancilla encoding or repeated nondestructive acquisition is free. These are changes of the measurement architecture, discussed in [acquisition and control](acquisition-and-control.md).

The parameter range is $`0\leq q\leq1/2`$. A known bit error above one half can be relabeled. At $`q=1/2`$ every report is independent of the input, so discrimination is impossible. The asymptotic matching theorem uses fixed $`0\lt q\lt 1/2`$; the noiseless endpoint and vanishing-noise sequences are treated separately.

## 2. The quantities controlling the record

Define

```math
s=1-2q,\qquad a=1-q,\qquad
b=(1-q)^2+q^2=\frac{1+s^2}{2}.
```

A specified reported outcome along signed Bloch axis $`u`$ has effect

```math
F_s(u)=\frac{I+s\,u\cdot\sigma}{2}.
```

For a fixed complete adaptive branch, the effect on one input copy is the tensor product of these factors. Fixing the reported branch fixes every chosen axis, even when the choices used earlier reports. Summing over the unobserved true outcomes gives the noisy effects above. The maximally mixed state assigns probability $`1/d`$ to each fully measured deterministic branch.

The normalized product effect has purity $`b^n`$ and largest eigenvalue $`a^n`$. These are the quadratic and linear concentration scales. Their significance is statistical: the target-to-mixed likelihood of every possible local record is close to one. The existing average-case readout-flattening scale is credited to [Maciejewski, Puchała and Oszmaniec](../references/RELATED_WORK.md); the converse here needs a simultaneous bound after the target is known.

## 3. Result map

| Result | Quantifiers and consequence | Complete account |
|---|---|---|
| Uniform likelihood theorem | For every prescribed $`q`$, one Haar event controls all noisy product effects, their partial-record versions and convex mixtures. Failure probability is at most $`e^{-80n^2}`$. | [Uniform concentration](uniform-concentration.md) |
| Adaptive binary converse | Every permitted strategy, including interleaved copies and bounded stopping, satisfies a transcript relative-entropy bound proportional to $`N\delta_n^2`$. | [Binary sample law](binary-sample-law.md) |
| Matching binary rate | At fixed $`0\lt q\lt 1/2`$, the optimal copy count has exponential rate $`-\log b`$. A fixed basis and classical likelihood test attain that rate. | [Binary sample law](binary-sample-law.md) |
| Full fidelity threshold | Exact-target completeness and constant bad-state infidelity admit polynomial copies precisely at the scale $`nq_n=O(\log n)`$ for Haar-typical targets. Robust completeness has an explicit gap-dependent tolerance. | [Fidelity certification](fidelity-certification.md) |
| Polynomial-size target preparation | Suitable approximate state designs transfer the binary law; finite universal gate sets give polynomial-size preparation circuits. | [Circuit targets](circuit-targets.md) |
| Acquisition and coherent control | A depolarizing acquisition layer gives copywise separable-measurement hardness, with a global typical-error-span comparison in an explicit entropy regime. Additional local redundancy or coherent inversion changes the resource model. | [Acquisition and control](acquisition-and-control.md) |

### Uniform finite-size estimate

With the explicit conservative constant $`C=1024`$, let

```math
\delta_n(q)=C\left[n b^{n/2}+n^2a^n\right].
```

The simultaneous likelihood deviation is at most $`\delta_n(q)`$ on the event above. Both terms are retained at finite size. For fixed positive $`q`$, the second term is asymptotically smaller because $`a^2\lt b`$. This asymptotic simplification need not be numerically accurate for small noise and moderate $`n`$.

### Sharp binary exponential rate

Let $`N_{\mathrm{opt}}(\psi,q,\alpha)`$ be the minimum deterministic copy cap for which both errors are at most fixed $`0\lt \alpha\lt 1/2`$. For fixed $`q\in(0,1/2)`$, with probability tending to one exponentially over the Haar target,

```math
\frac{c_{q,\alpha}}{n^2 b^n}
\leq N_{\mathrm{opt}}(\psi,q,\alpha)
\leq C_{q,\alpha}b^{-n}.
```

Consequently,

```math
\frac{1}{n}\log N_{\mathrm{opt}}(\psi,q,\alpha)
\longrightarrow-\log b
```

in probability. This expression specifies the exponential rate, not a matched polynomial prefactor. The upper and lower bounds hold on the intersection of their separately quantified target events. The lower-bound event has failure at most $`e^{-80n^2}`$; the fourth-moment event used for the upper bound has failure exponentially small in $`n`$ at fixed $`q`$.

### Full fidelity certification

Fidelity here means $`F_\psi(\rho)=\langle\psi|\rho|\psi\rangle`$. At fixed bad-state infidelity and confidence, exact-target certification accepts $`\rho=\psi`$ and rejects every $`\rho`$ below the fidelity threshold. The maximally mixed alternative embeds the binary converse into this task. For sufficiency, an ideal nonadaptive local-Pauli score is inverted through the known binary symmetric channel. Its range grows at most as $`s^{-n}`$, giving sample overhead at most $`s^{-2n}`$.

The resulting polynomial criterion is $`nq_n=O(\log n)`$. If $`nq_n/\log n\to\infty`$, the converse is superpolynomial. If the ratio is merely unbounded, it rules out one polynomial cap valid for all sufficiently large $`n`$, along a subsequence. A robust good-state promise requires $`\gamma\varepsilon_{\mathrm b}>\varepsilon_{\mathrm g}`$, with $`\gamma`$ a valid verification-gap lower bound. No matched fixed-noise exponent is asserted for this composite problem.

## 4. What the mechanism establishes

The result controls a measurement chosen with complete target knowledge. An average over targets for each fixed measurement would leave open the possibility that a target-specific measurement recovers a strong signal. The product-effect net removes that possibility for this acquisition model. The full-transcript hybrid argument then covers feedback across all copies without assuming independent observed records.

The binary upper bound is constructive at the information-theoretic level: choose one basis, compute the target's noisy outcome distribution, and use the likelihood-ratio test. Evaluating that distribution can require exponential classical work. Polynomial-size preparation of a target from an approximate design removes an exponential preparation requirement for the binary separation, while preserving the unrestricted classical-advice converse. It does not establish efficient likelihood evaluation or transfer the ideal full-fidelity gap automatically.

The architecture matters. Repeated ideal nondestructive reporting and majority decoding can reduce a fixed detector error to order $`1/n`$ using order $`\log n`$ reports per site. Coherent local fanout can supply equivalent redundancy at additional ancilla and gate cost. A supplied preparation circuit can be inverted before detection, again with charged coherent gates. A noise layer acting before such control is a different experiment. These comparisons locate the lost resource: information available before irreversible local acquisition.

## 5. Reading and verification

The [science index](README.md) gives the dependency order. [Related work](../references/RELATED_WORK.md) separates inherited ingredients from the target-informed adaptive statement. The [reproduction guide](../code/README.md) runs independent finite checks of the Haar moment identities, noisy adaptive instruments, interleaved transcript factorization and classical score inversion. Finite checks corroborate formulas and implementations; the asymptotic claims rest on the proofs.
