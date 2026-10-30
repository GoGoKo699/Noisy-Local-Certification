# From Watrous to noisy local certification

**Educational anchor:** John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018). The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the manuscript and individual chapters. The section and theorem labels below refer to that author-hosted manuscript; its [contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf) provide the navigation. The book is linked here, not redistributed.

This project asks how much information survives when a known quantum state is accessed through one imperfect local report from each qubit. Watrous supplies the language of states, measurements, discrimination and Haar randomness. The project's proofs connect those foundations to a restriction on measurement resources.

Start with [the experiment and result map](../science/model-and-results.md). Use the selections below when their concepts arise in the [30-milestone map](MILESTONES.md): M01–M12 assemble the background, and M13–M30 develop the result and its boundaries. This bridge explains the source conventions and the steps beyond the book; the milestone map owns the dependency order and understanding targets.

## Selected readings

The following are selections within one anchor. Reading whole chapters is unnecessary.

| Purpose | Exact source location | What to take into this project |
|---|---|---|
| Look up mathematical notation as needed | [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), §1.1.2, **Linear operators**; §1.1.3, **Operator decompositions and norms**; §1.2.2, **Probability theory** | Tensor products, positive operators, traces, operator norms and expectations. These are reference sections, not a separate preliminary course. |
| Describe a state and its classical report | [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf), §2.1.2, **Quantum states of registers**; §2.3.1, **Two equivalent definitions of measurements** | A density operator specifies outcome probabilities; a measurement can be represented by positive effects summing to the identity. |
| Understand the binary decision task | [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), §3.1.1, **Discriminating between pairs of quantum states**, especially Theorem 3.4 | The unrestricted measurement benchmark, and why restricting the available measurements changes the operational question. |
| Read the statistical converse | [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), §5.1.1, **Definitions of classical entropic functions**, especially Definition 5.3; §5.1.2, **Properties of classical entropic functions**, especially Lemma 5.4 and Theorem 5.13 | Relative entropy compares transcript distributions. The final decision is a coarse-graining of a transcript, so its separation cannot exceed the information in that transcript. |
| Compute with a generic pure target | [Chapter 7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), §7.1.1, **The subspace of permutation-invariant vectors**; §7.2.1, **Uniform spherical measure and Haar measure**, especially Theorem 7.22 and Lemma 7.24 | Haar-random unit vectors, normalized Gaussian sampling, and tensor moments expressed through the symmetric subspace. |

Additional selections enter only with their corresponding extensions:

| Project branch | Selection from the same book | Connection and limit |
|---|---|---|
| Fidelity certification | [§3.2, **The fidelity function**](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf), beginning with Definition 3.11 | Translate the fidelity convention below before reading a certification promise. The book does not supply this project's local verifier gap. |
| Acquisition noise | [§2.2, **Quantum channels**](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf): the definitions in §2.2.1 and the replacement-channel example in §2.2.3, **Examples of channels and other mappings** | Distinguish a channel acting on the quantum state from classical corruption after measurement. |
| Separable acquisition measurements | [Chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf), §6.1.1, **Separable operators and states**; §6.1.3, **Separable and LOCC measurements** | Positive sums of product effects describe a larger class than locally implementable measurements. Here separability is required across all input sites of one copy. |
| Global acquisition comparison | [§5.3.1, **Classical source coding**](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf), focusing on typical sequences | Typical noise strings can have high probability while spanning a small part of the quantum state space. |
| Circuit-design accuracy | [§3.3.2, **The completely bounded trace norm**](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Recognize the channel norm used when converting a research theorem about unitary designs into a state-moment guarantee. |
| Concentration context | [§7.3.1, **Lévy's lemma and Dvoretzky's theorem**](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf), optionally | Background for the idea of concentration. The proof here develops a particular high-moment bound and product net; it does not invoke this section as a ready-made proof of the required uniform estimate. |

## Notation and conventions

| In Watrous | In this repository |
|---|---|
| A unit vector $`u`$ and its pure-state operator $`uu^*`$ | The target vector is $`\lvert\psi\rangle`$; $`\psi`$ also denotes $`\lvert\psi\rangle\langle\psi\rvert`$ inside a trace. |
| The adjoint $`A^*`$ and identity $`1_{\mathcal X}`$ | $`A^\dagger`$ or $`A^*`$, and $`I`$. The input space is $`(\mathbb C^2)^{\otimes n}`$ with dimension $`d=2^n`$. |
| A measurement written as a function $`\mu(y)`$ | A POVM effect $`M_y`$, or a branch effect $`H_i(t)`$. Its probability is $`\mathrm{tr}(\rho M_y)`$. |
| The trace norm $`\lVert A\rVert_1`$ and spectral norm $`\lVert A\rVert`$ | $`\lVert A\rVert_1`$ and $`\lVert A\rVert_\infty`$. The trace-norm design error is unhalved. |
| Fidelity $`F(\rho,\sigma)=\lVert\sqrt\rho\sqrt\sigma\rVert_1`$ | Target fidelity $`F_\psi(\rho)=\langle\psi\rvert\rho\lvert\psi\rangle=F(\psi,\rho)^2`$. A promise on one convention must be converted before using the other. |
| Base-2 $`\log`$ in entropy and relative entropy | The binary proofs use natural logarithms: $`D_{\mathrm{nat}}=(\ln 2)D_{\mathrm{bits}}`$. The acquisition entropy $`H_4`$ explicitly uses bits. |
| A tensor-power index in the symmetric-subspace formulas | Use $`t`$ for moment order here. It is distinct from the number $`n`$ of physical qubits and the copy budget $`N`$. |

For classical distributions, total variation is one half of their $`\ell_1`$ distance. Likewise, the usual operational trace distance between states is one half of their trace-norm difference. The approximation parameter in [circuit targets, §1](../science/circuit-targets.md#1-moment-convention-and-result) bounds the full trace norm, without that factor.

There is also a useful normalization distinction. A physical POVM effect need not have trace one. When comparing it with the maximally mixed state $`\tau=I/d`$, its likelihood ratio is

```math
\frac{\mathrm{tr}(\psi M)}
     {\mathrm{tr}(\tau M)}
=d\,\mathrm{tr}\!\left(\psi\,\frac{M}{\mathrm{tr}M}\right),
\qquad \mathrm{tr}M>0.
```

The normalized operator is a tool for the likelihood calculation; it need not be an outcome of the original POVM.

## A first translation: one imperfect report

Measure a qubit in the computational basis and flip its ideal outcome with probability $`q`$. The effect for a reported zero is

```math
F_0=(1-q)\lvert0\rangle\langle0\rvert
       +q\lvert1\rangle\langle1\rvert
    =\frac{I+(1-2q)Z}{2}.
```

At $`q=0.1`$, this effect has eigenvalues $`0.9`$ and $`0.1`$. The report-zero probability is $`0.9`$ on the target $`\lvert0\rangle`$ and $`0.5`$ on $`I/2`$. Its purity is $`0.9^2+0.1^2=0.82`$.

For a specified branch measuring all $`n`$ qubits, the product effect therefore has purity $`b^n`$, where $`b=(1-q)^2+q^2`$, and largest eigenvalue $`(1-q)^n`$. These two quantities enter the concentration proof. The unknown input can be entangled: it is the **branch effect**, not the state or its observed reports, that factorizes. For adaptive measurements, fixing the reported branch fixes its chosen axes.

This example also explains why noise alone does not imply a universal exponential cost. The target $`\lvert0\rangle^{\otimes n}`$ can already be distinguished from $`I/2^n`$ by repeatedly sampling one site. The theorem concerns typical targets in its specified ensembles. [The model](../science/model-and-results.md) and [uniform-concentration proof](../science/uniform-concentration.md) make those quantifiers explicit.

## How the experimental model changes the textbook question

Theorem 3.4 of Watrous optimizes over unrestricted quantum measurements. For the clean pair $`\psi`$ and $`I/d`$, measuring $`\{\psi,I-\psi\}`$ accepts the target with certainty and accepts $`I/d`$ with probability $`1/d`$. The project instead limits each input qubit to one local projective measurement with one corrupted classical report. Target knowledge and arbitrary classical feedback remain available, but they do not implement the global projector.

The same single-use report statistics arise if a qubit first undergoes

```math
\mathcal D_q=(1-2q)\mathrm{id}+2q\,\Omega,
\qquad
\Omega(X)=\mathrm{tr}(X)\frac I2,
```

and is then measured ideally. Here $`\Omega`$ is the completely depolarizing channel from the book. The replacement weight is $`2q`$, although the detector bit-flip probability is $`q`$. This equality concerns the specified one-use measurement statistics. Repeated nondestructive reporting after a clean measurement, or encoding a report into fresh ancillas before detection, has different resources and does not reverse noise that already acted on the input state.

For the acquisition extension, each copy may undergo an arbitrary separable POVM across its sites; classical adaptation between copies is allowed. This extension does not assert a converse for joint quantum memories spanning copies. The [acquisition and control account](../science/acquisition-and-control.md) states and compares these experiments.

## Steps supplied by the project

The book establishes the foundations; the following arguments are supplied in the scientific account.

| Bridge beyond the anchor | What must still be proved | Canonical source |
|---|---|---|
| From Haar averages to a measurement chosen after seeing the target | A fixed-effect expectation is insufficient. A centered Gaussian moment estimate and a product net control all allowed effects on one common target event. | [Uniform concentration, §§2–4](../science/uniform-concentration.md) |
| From local branch likelihoods to an adaptive copy lower bound | Complete transcript effects factor by input copy. Replacing one copy at a time produces normalized hybrid transcript laws and the exact KL identity, even when copies are interleaved. | [Binary sample law, §2](../science/binary-sample-law.md#2-a-transcript-identity-that-covers-arbitrary-interleaving) |
| From a converse to the optimal binary exponential rate | Exact fixed-basis second and fourth moments, followed by a Hellinger/likelihood argument, supply the matching upper rate. The polynomial prefactors need not match. | [Binary sample law, §§3–5](../science/binary-sample-law.md) |
| From the binary promise to fidelity certification | A verifier gap and bounded local score are needed. Classical inversion of the detector channel supplies sufficiency; the mixed alternative supplies necessity. Robust completeness requires a positive gap $`G=\gamma\varepsilon_{\mathrm b}-\varepsilon_{\mathrm g}`$. | [Fidelity certification](../science/fidelity-certification.md) |
| From Haar targets to finite circuit descriptions | High moments must survive the stated approximation norm. The proof tracks moment order, exponentially small design error, circuit length and gate precision. This transfers the binary theorem, not automatically the full-fidelity verifier gap. | [Circuit targets](../science/circuit-targets.md) |
| From product effects to alternative control architectures | Normalize and convexly combine separable effects; construct the global typical-error-span test; charge extra reports, ancillas and coherent gates explicitly. | [Acquisition and control](../science/acquisition-and-control.md) |

One central step is worth keeping visible. Let $`\delta_n`$ bound the deviation of every normalized one-copy branch likelihood from one on the common target event. For the full transcript laws $`P`$ (all target copies), $`Q`$ (all mixed copies), and $`P^{(i)}`$ (only copy $`i`$ replaced by the mixed state), the branch factorization gives

```math
D(P\|Q)=\sum_{i=1}^{N}D(P\|P^{(i)})
\leq N\delta_n^2.
```

This is not an assumption that the adaptive records are independent. Each hybrid is the law of the same protocol with one different physical input; its normalization is essential. The [proof](../science/binary-sample-law.md#lemma-2-hybrid-relative-entropy-identity) supplies that justification.

## Research dependencies beyond the anchor

These papers serve attribution and proof verification, rather than additional educational anchors. The [reference list](../references/REFERENCES.md) gives precise versions and used locations.

| Research ingredient or comparison | Role |
|---|---|
| [Maciejewski, Puchała and Oszmaniec](../references/REFERENCES.md#average-case-distances) | Existing average-case readout suppression and the noisy-product collision factor. The project adds the simultaneous target-informed quantifier and optimized copy law. |
| [Low](../references/REFERENCES.md#design-concentration) | Prior high-moment design transfer and product-net methods. The particular noisy-effect estimates are derived locally. |
| [Brandão, Harrow and Horodecki](../references/REFERENCES.md#circuit-designs) | The imported polynomial circuit-design theorem; the local account derives the needed norm conversion and parameter costs. |
| [Du and collaborators](../references/REFERENCES.md#du) | The ideal conditional-fidelity observable, bounded local score and typical-target verifier gap used in the full-certification branch. |
| [Liu and collaborators](../references/REFERENCES.md#scrambling-under-noise), and [Lupo, Wilde and Lloyd](../references/REFERENCES.md#noisy-data-hiding) | Prior noisy distinguishability and data-hiding context for the acquisition comparison; see [the exact scope comparison](../references/RELATED_WORK.md). |

For the complete argument, follow the [science index](../science/README.md). For evidence about finite implementations and formulas, use the [reproduction guide](../code/README.md); those checks complement the analytical proofs.
