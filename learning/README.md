# Learning the local-noise mechanism

The experiment begins with a source that repeatedly prepares the same quantum state. A complete classical description of the desired pure target is available. Each input qubit supplies at most one local measurement report, and a calibrated detector may flip that report. The scientific question is how many independent source copies are needed to make a reliable decision.

The shared [30-milestone map](MILESTONES.md) organizes this story into 12 foundation milestones and 18 milestones developing the contribution. Its single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [Watrous bridge](WATROUS_BRIDGE.md) identifies the useful sections, translates conventions and supplies the steps that the textbook does not cover. The [scientific index](../science/README.md) provides the direct route to complete statements and proofs.

## 1. Begin with one imperfect bit

Consider a single qubit, with target state $\lvert0\rangle$ and alternative $I/2$. Measure in the computational basis and report the outcome through an independent bit-flip channel with probability $q$. The distributions of the reported bit are

$$
P_\psi=(1-q,q),\qquad P_\tau=(1/2,1/2).
$$

For $q=0.1$, the target produces a zero with probability $0.9$, while the maximally mixed state produces a zero with probability $0.5$. The total variation distance is $0.4$. Repeating this experiment a number of times independent of any larger system size suffices for a fixed error probability. The same observation applies to one chosen qubit of the product target $\lvert0\rangle^{\otimes n}$.

This example makes the typical-target assumption consequential. Constant detector noise alone does not make every known target hard. The result concerns targets whose distinguishability is distributed through generic many-qubit correlations. The [model](../science/model-and-results.md#1-the-experiment-and-its-resources) specifies both the target ensemble and the permitted measurement resources.

## 2. Move the reporting channel into the measurement effect

Let $\Pi$ be the ideal rank-one effect for one reported outcome, and define $s=1-2q$. Including the reporting error in the Born-rule calculation gives

$$
E=(1-q)\Pi+q(I-\Pi)=qI+s\Pi.
$$

The eigenvalues of this positive operator are $1-q$ and $q$, and its trace is one. Its two useful spectral scales are

$$
a=1-q,\qquad b=(1-q)^2+q^2.
$$

For a complete local record on $n$ qubits, the corresponding effect is a tensor product of such factors. Consequently its operator norm is $a^n$ and its squared Hilbert–Schmidt norm is $b^n$. These two scales appear separately in the finite-size concentration bound. Keeping both is necessary when the reporting noise varies with system size.

Adaptive measurements still have product effects along each fixed recorded branch. The axis chosen later on that branch has already been determined by its earlier reported outcomes. Summing the branches recovers the whole protocol. The [uniform concentration proof](../science/uniform-concentration.md) and [transcript construction](../science/binary-sample-law.md#2-a-transcript-identity-that-covers-arbitrary-interleaving) make this statement precise, including unmeasured sites and stopping.

## 3. Explain why typical local records flatten

Write $d=2^n$, and let $E_y$ be one complete product effect. Under the maximally mixed state its probability is $1/d$. Under the pure target its relative likelihood is

$$
\ell_y=d\langle\psi\vert E_y\vert\psi\rangle.
$$

The second Haar moment gives

$$
\mathbb E_\psi\ell_y=1,\qquad
\operatorname{Var}_\psi(\ell_y)
=\frac{d b^n-1}{d+1}.
$$

At fixed nonzero noise, the variance becomes small exponentially in the number of qubits. Most targets therefore make this particular local record look nearly maximally mixed. Knowing the target allows the experimenter to choose a different measurement, however. A statement for one measurement chosen before the target does not settle that optimization.

The project's uniform theorem closes that quantifier gap. Higher moments and a finite product net establish one high-probability target event on which every allowed product effect is controlled simultaneously. On that event, choosing axes after seeing the target or earlier data cannot select an uncontrolled effect. The map follows this transition from an individual effect to a universal measurement statement in M13–M15.

## 4. Account for all copies, even when they are interleaved

A protocol may begin measuring one copy, inspect a different copy, and use both records to decide what to do next. Its complete classical transcript still has one product effect for each input copy. Let $P_\psi$ be the transcript law when every copy contains the target, $P_\tau$ the law when every copy is maximally mixed, and $P^{(i)}$ the law of the same physical protocol with only copy $i$ replaced by the maximally mixed state. The protocol keeps the same target description in every experiment.

The normalized hybrid laws yield the identity

$$
D(P_\psi\Vert P_\tau)
=\sum_{i=1}^{N}D(P_\psi\Vert P^{(i)}).
$$

Each summand is controlled by the single-copy uniform estimate. Thus the total statistical evidence grows at most linearly in the worst-case number of attempted copies. Discarding a record does not refund the copy that produced it. This is the mechanism behind the converse, including arbitrary permitted classical feedback. M16–M18 connect the transcript factorization to the sample lower bound; [the binary proof](../science/binary-sample-law.md) supplies normalization and support details.

A fixed computational basis and a likelihood test achieve the same exponential rate. The achievability proof needs more than the mean signal: exact fourth moments show that a typical target has enough signal, and a Hellinger bound turns it into a test with both errors controlled. This is the M19–M22 route. The number of copies is optimized while classical likelihood computation remains unrestricted.

## 5. Separate binary recognition from fidelity certification

The binary experiment promises either the target or one specific alternative. Fidelity certification must also reject arbitrary states whose overlap with the target is too small. In this repository the fidelity convention for a pure target is

$$
F_\psi(\rho)=\langle\psi\vert\rho\vert\psi\rangle.
$$

Watrous uses the root-fidelity convention in his general definition; its square equals this expression for a pure target. The [bridge](WATROUS_BRIDGE.md) keeps that translation explicit.

For the full task, an attributed ideal verification score is corrected by inverting the classical reporting channel. Inversion preserves its expectation and enlarges its range. That range controls the number of samples required for concentration. Together with the binary converse, the argument gives the polynomial-copy threshold $nq_n=O(\log n)$ for exact-target completeness and fixed bad-state infidelity.

Robust good-state promises require $\gamma\epsilon_{\mathrm{bad}}-\epsilon_{\mathrm{good}}>0$, where $\gamma$ is a valid lower bound on the ideal verification gap. M23–M25 explain the task, score and threshold. The [fidelity chapter](../science/fidelity-certification.md) states the precise probabilities and imported theorem. A matching fixed-noise exponent for the composite fidelity task is not established.

## 6. Put preparation and control back into the experiment

M26–M29 examine which conclusions survive when the architecture changes. Sufficiently accurate state designs transfer the binary theorem to a polynomial-size preparation ensemble. That transfer has a quantitative high-order moment requirement; a few random-circuit simulations do not establish it. It also does not automatically transfer the ideal full-fidelity verification gap.

Noise placement determines what additional control can accomplish. A supplied coherent inverse applied before noisy detection permits a different binary experiment, with its gates counted. Repeated nondestructive reports or local ancilla encoding supply redundancy that the one-use model does not have. If depolarization has already acted on the input before control, a global typical-error-span measurement provides another comparison, under a sufficient entropy condition and without an efficient-implementation claim. The [resource summary](../science/acquisition-and-control.md#7-resource-summary) places these assumptions side by side.

M30 integrates the result, attribution, evidence and limits. The common route ends with an understanding of why a known state can be difficult to recognize through a restricted noisy interface, which rate has been matched, and which changes of physical access alter the conclusion.

## Reading routes

| Purpose | Route |
|---|---|
| Build the full conceptual picture | This introduction → [milestones](MILESTONES.md) → [Watrous bridge](WATROUS_BRIDGE.md) alongside the relevant science |
| Check the main theorem | [Model and claims](../science/model-and-results.md) → [uniform bound](../science/uniform-concentration.md) → [binary sample law](../science/binary-sample-law.md) |
| Examine full certification | [Fidelity task and proof](../science/fidelity-certification.md) → [attribution](../references/RELATED_WORK.md) |
| Reproduce finite identities | [Verification guide](../verification/README.md) → [checking implementation](../code/README.md) |

The milestones are shared scientific understanding targets. Individual study sessions and assessment records are separate from this repository.
