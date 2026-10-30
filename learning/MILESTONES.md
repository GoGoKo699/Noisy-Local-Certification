# Thirty milestones for noisy local certification

This map describes the understanding needed to connect a single imperfect detector report to the project's optimal binary copy law, fidelity threshold and measurement-resource comparisons. Its targets depend on the scientific argument and are the same for every reader. They cover the connected account; the canonical science pages retain the detailed proofs and finite constants.

The single educational anchor is John Watrous, *The Theory of Quantum Information* (2018). The [author's chapter index][Watrous] and [table of contents][WContents] identify the sections cited below. The [Watrous bridge](WATROUS_BRIDGE.md) translates their notation and explains which project-specific steps must be supplied separately. Chapter links refer to the author-hosted source, which is linked rather than copied into this repository.

## Allocation and dependency structure

The map allocates **12 milestones to background/preliminaries** and **18 to narrative/innovation**. The background must connect three kinds of objects: quantum effects, classical statistical evidence and random target states. Twelve targets give these prerequisites a coherent experimental meaning before the proof begins. The longer narrative phase follows the two sides of the binary theorem, then integrates the distinct fidelity and physical-resource consequences. This allocation reflects the argument's dependencies rather than the textbook's chapter order.

| Phase | Milestones | Local-to-global progression |
|---|---|---|
| Background/preliminaries | M01–M12 | A state and one detector report → a multipartite adaptive experiment → its statistical task and quantifiers |
| Narrative/innovation | M13–M30 | One-effect concentration → a converse for every allowed transcript → matching binary performance → certification and architecture comparisons |

Dependencies listed in an entry are earlier milestones whose ideas it uses. They identify the scientific connections, not a learner's status. M12 synthesizes the background; M22 integrates the binary proof; M30 integrates the full project. The later branches remain connected: M23–M25 treat composite fidelity certification, M26–M27 treat preparation and coherent access, and M28–M29 locate the noise and redundancy resources.

All source pointers distinguish textbook foundations from the canonical project derivation. A Watrous pointer does not attribute this project's noisy-product or adaptive-transcript theorem to the textbook. Imported research ingredients and their precise scope remain in the linked science pages and [related-work account](../references/RELATED_WORK.md).

## Phase I — Background/preliminaries

### M01 — States, known targets and independent copies

- **Central question:** What is physically supplied when a verifier knows the desired state but receives an uncertain source?
- **Understanding target:** Distinguish a pure-state vector, its rank-one density operator, a general density operator and the maximally mixed state. Explain why classical knowledge of a target and possession of independent quantum copies are different resources.
- **Dependencies and story role:** No earlier milestone. Establishes the single-system objects from which the experiment is built.
- **Conceptual connection:** A state description determines Born probabilities; it does not itself implement a measurement or provide extra input copies.
- **Source pointers:** Watrous [§2.1.2][W2]; project [model §1](../science/model-and-results.md#1-the-experiment-and-its-resources).

### M02 — Projective measurements and reported events

- **Central question:** How does one qubit become a classical observation?
- **Understanding target:** Explain a binary rank-one projective measurement, its chosen Bloch axis and its outcome probabilities. Distinguish a measurement effect, which specifies an event's probability, from an instrument, which also describes the remaining quantum system.
- **Dependencies and story role:** Uses M01. Introduces the local operation whose permitted uses determine the resource model.
- **Conceptual connection:** The Born rule translates a physical measurement into an operator calculation, while destructiveness limits which later observations remain available.
- **Source pointers:** Watrous [§§2.3.1–2.3.2][W2]; project [binary protocol §1](../science/binary-sample-law.md#1-protocol-and-error-conventions) and [acquisition §1](../science/acquisition-and-control.md#1-two-explicitly-located-noise-models).

### M03 — A binary symmetric detector channel

- **Central question:** How does an independently flipped report change a measurement effect?
- **Understanding target:** Derive the reported effect as the weighted sum of the two ideal projectors and interpret the contraction parameter $`s=1-2q`$. Separate a hidden ideal outcome from the corrupted outcome actually available for feedback.
- **Dependencies and story role:** Uses M02. Adds noise to the single-site experiment before considering many sites.
- **Conceptual connection:** Classical postprocessing acts on quantum effects through linearity; its uncertainty can be represented without pretending the true outcome is observed.
- **Source pointers:** Watrous [§§2.2.1, 2.3.1][W2]; project [model §2](../science/model-and-results.md#2-the-quantities-controlling-the-record) and [acquisition §1](../science/acquisition-and-control.md#1-two-explicitly-located-noise-models).

### M04 — Tensor products without independent outcomes

- **Central question:** Why can a local measurement have a product effect even when its input is entangled?
- **Understanding target:** Distinguish tensor structure of an effect from independence of its outcome probabilities. Explain how the expectation of a product effect on an entangled input retains correlations, whereas independently supplied source copies have a product input state.
- **Dependencies and story role:** Uses M01–M03. Connects local detector factors to an entire input copy.
- **Conceptual connection:** Locality constrains the operator representing an event; it does not erase correlations already present in the state.
- **Source pointers:** Watrous [§1.1.1][W1], [§§2.1.2–2.1.3][W2]; project [uniform notation §1](../science/uniform-concentration.md#1-statement-and-notation) and [transcript Lemma 1](../science/binary-sample-law.md#lemma-1-product-effects-for-a-complete-recorded-transcript).

### M05 — The two spectral scales of a noisy effect

- **Central question:** Which properties of a noisy product effect control its fluctuations over targets?
- **Understanding target:** Interpret trace normalization, purity and largest eigenvalue. Relate the local eigenvalues $`1-q`$ and $`q`$ to the product scales $`b^n`$ and $`a^n`$, where $`a=1-q`$ and $`b=(1-q)^2+q^2`$.
- **Dependencies and story role:** Uses M03–M04. Identifies the quantitative objects that the concentration proof must retain.
- **Conceptual connection:** The Hilbert–Schmidt scale measures aggregate spectral weight, while the operator norm controls the largest contribution. They enter different terms of the finite-size bound.
- **Source pointers:** Watrous [§1.1.3][W1]; project [uniform Corollary 3](../science/uniform-concentration.md#corollary-3-moments-for-one-noisy-product-effect) and [model §2](../science/model-and-results.md#2-the-quantities-controlling-the-record).

### M06 — Adaptation, interleaving and the copy budget

- **Central question:** What can the verifier change after seeing earlier reports, and what resource is being counted?
- **Understanding target:** Describe target-dependent axes, qubit order, classical feedback, stopping and interleaving of unread qubits from different copies. Explain the deterministic cap on all accessed copies and the distinction between classical control and coherent coupling of quantum inputs.
- **Dependencies and story role:** Uses M02–M04. Assembles the local operations into the full allowed protocol class.
- **Conceptual connection:** A strong sample lower bound must cover every permitted use of target information and past reports, including discarded attempts, without silently granting extra detector uses or ancilla encoding.
- **Source pointers:** Watrous [§§2.2.1, 2.3.2][W2] for operations; project [binary protocol §1](../science/binary-sample-law.md#1-protocol-and-error-conventions) for the precise restrictions.

### M07 — Binary discrimination and two conditional errors

- **Central question:** What does a successful decision between the target and the maximally mixed state require?
- **Understanding target:** Define the two hypotheses, false rejection, false acceptance and the minimum deterministic copy budget. Distinguish a copy-complexity guarantee from a classical runtime guarantee and an average-prior error from a bound on each conditional error.
- **Dependencies and story role:** Uses M01 and M06. Gives the experimental architecture a precise statistical goal.
- **Conceptual connection:** State discrimination becomes a classical decision problem after measurement, but the permitted measurement family determines which outcome distributions can be produced.
- **Source pointers:** Watrous [§3.1.1][W3]; project [binary protocol §1](../science/binary-sample-law.md#1-protocol-and-error-conventions).

### M08 — Likelihoods and accumulated statistical evidence

- **Central question:** How can closeness of record distributions limit every classical decision rule?
- **Understanding target:** Interpret likelihood ratios, classical relative entropy, chi-square divergence and Hellinger affinity as different measures of statistical evidence. Explain why forgetting records cannot improve distinguishability and why independent repetitions multiply affinity.
- **Dependencies and story role:** Uses M07. Supplies the statistical language for both the converse and the attainable test.
- **Conceptual connection:** Quantum effects produce probability laws; divergence inequalities then bound the information available to unrestricted classical processing. The project's relative entropy uses natural logarithms.
- **Source pointers:** Watrous [§§5.1.1–5.1.2][W5] and [§3.2][W3] for classical fidelity; project [binary §2](../science/binary-sample-law.md#2-a-transcript-identity-that-covers-arbitrary-interleaving) and [§4](../science/binary-sample-law.md#4-from-chi-square-divergence-to-a-test-with-controlled-errors) for the needed inequalities.

### M09 — Fidelity promises and composite alternatives

- **Central question:** How does certifying a target against all sufficiently different states exceed a binary promise?
- **Understanding target:** Interpret the good-state and bad-state fidelity regions, their intervening unconstrained region and exact-target completeness. Translate between the project's pure-target overlap and the square of Watrous's root-fidelity convention.
- **Dependencies and story role:** Uses M01 and M07. Places the binary problem inside the more general certification task.
- **Conceptual connection:** Rejecting one known alternative is necessary for a fidelity certificate but does not supply soundness against every low-fidelity state.
- **Source pointers:** Watrous [§§3.2–3.2.1][W3]; project [fidelity §1](../science/fidelity-certification.md#1-task-promises-and-detector-model) and [binary §6](../science/binary-sample-law.md#6-endpoints-and-certification-scope).

### M10 — Haar targets and tensor moments

- **Central question:** What does a typical target mean, and how can averages over all pure states be calculated?
- **Understanding target:** Explain uniform spherical measure, its relation to Haar-random unitaries and the normalized Gaussian representation. Interpret the symmetric-subspace formula for tensor moments and distinguish probability over targets from a testing error on repeated copies of one fixed target.
- **Dependencies and story role:** Uses M01, M04 and M05. Introduces the target ensemble and the moment identities used by both sides of the proof.
- **Conceptual connection:** Unitary symmetry replaces integration over an enormous state space with structured operator expressions; it does not assert the result for every state.
- **Source pointers:** Watrous [§§7.1.1, 7.2.1, including Lemma 7.24][W7]; project [uniform §2](../science/uniform-concentration.md#2-a-normalized-gaussian-moment-bound) and [binary §3](../science/binary-sample-law.md#3-fixed-basis-statistics-and-exact-haar-moments).

### M11 — Fixed-measurement averages and uniform statements

- **Central question:** Why is a typical outcome law for each fixed measurement insufficient when the target is already known?
- **Understanding target:** Distinguish “for each fixed effect, most targets” from “for most targets, every allowed effect.” Explain the purpose of high moments, a finite covering net and continuity in establishing the second quantifier order.
- **Dependencies and story role:** Uses M05, M06 and M10. Identifies the logical gap the central concentration theorem must close.
- **Conceptual connection:** The measurement can depend on the target. A simultaneous event makes that optimization harmless to the bound without enumerating all adaptive decision trees.
- **Source pointers:** Watrous [§1.2.2][W1] and [§7.3.1][W7] as probability and concentration context; project [uniform §3](../science/uniform-concentration.md#3-the-product-net-and-proof-of-theorem-1) and [related work §2](../references/RELATED_WORK.md#2-fixed-noisy-measurements-already-exhibit-the-same-collision-scale).

### M12 — The complete question and its quantifiers

- **Central question:** What exactly must be established to show that known generic targets become expensive to test locally?
- **Understanding target:** Assemble the independent-copy source, complete target advice, calibrated independent reports, one-use architecture, allowed feedback, confidence and target typicality into one statement. Identify the separate roles of a universal lower bound, an attainable binary test and a composite-fidelity consequence.
- **Dependencies and story role:** Integrates M01–M11 and completes the background phase.
- **Conceptual connection:** The result concerns information obtainable under a specified acquisition architecture. It can coexist with inexpensive ideal measurements, unrestricted classical computation and stronger coherent measurement capabilities.
- **Source pointers:** Watrous [Chapter 2][W2] and [Chapter 3][W3] for the measurement/discrimination framework; project [model §§1–4](../science/model-and-results.md) and [science reading route](../science/README.md).

## Phase II — Narrative/innovation

### M13 — Concentrating one noisy product effect

- **Central question:** How do the two spectral scales bound the likelihood fluctuation for one effect?
- **Understanding target:** Explain centering by the maximally mixed state, diagonalizing a Gaussian quadratic form and controlling its high moments. Identify why independence of Gaussian radius and direction gives an exact normalization relation and preserves both the quadratic and linear terms.
- **Dependencies and story role:** Uses M05, M10 and M11. Begins the narrative with the local probabilistic ingredient.
- **Conceptual connection:** A quantum expectation becomes a weighted sum of independent centered exponential variables. The project derives its specific moment estimate rather than substituting a generic concentration slogan.
- **Source pointers:** Watrous [§1.2.2][W1] and [§7.2.1][W7]; project [uniform Lemma 2 and Corollary 3](../science/uniform-concentration.md#2-a-normalized-gaussian-moment-bound).

### M14 — One target event for all noisy product effects

- **Central question:** How does a bound for one effect become valid for every target-dependent choice of axes?
- **Understanding target:** Connect the product-net size, moment order, union bound and tensor-product continuity estimate. Read the resulting event as simultaneous over effects for a prescribed noise parameter, with failure probability over the target alone; retain both terms in the finite-size deviation.
- **Dependencies and story role:** Uses M11 and M13. Turns the local concentration ingredient into the first global theorem.
- **Conceptual connection:** A net describes the family of possible branch effects. This avoids counting the much larger family of whole adaptive protocols.
- **Source pointers:** Watrous [§1.2.1][W1] and [§7.3.1][W7] for mathematical context; project [uniform Theorem 1](../science/uniform-concentration.md#theorem-1-uniform-noisy-product-bound) and [its proof](../science/uniform-concentration.md#3-the-product-net-and-proof-of-theorem-1).

### M15 — Unread sites, partial records and convexity

- **Central question:** Why does the same event control a branch that stops before every qubit is measured?
- **Understanding target:** Normalize a partial-record effect by its trace, recognize an unread site as an identity factor becoming $`I/2`$, and express interior Bloch vectors as convex mixtures. Explain why the likelihood bound survives these mixtures without a new probability event.
- **Dependencies and story role:** Uses M04 and M14. Extends the uniform theorem to the effects actually needed by stopping and later measurement-class comparisons.
- **Conceptual connection:** Trace normalization removes the trivial probability scale of a branch; convexity preserves its deviation bound even when a site contains less information.
- **Source pointers:** Watrous [§1.2.1][W1] and [§2.3.1][W2]; project [uniform §§3–4](../science/uniform-concentration.md#4-partial-measurement-records).

### M16 — A complete transcript fixes every local effect

- **Central question:** What factorization survives when copies and measurement choices are interleaved?
- **Understanding target:** Explain why fixing the random seed and terminal reported path fixes all selected sites and axes. Factor the corresponding effect by input copy, sum inaccessible true outcomes correctly and include unread sites and unused copies through identity effects.
- **Dependencies and story role:** Uses M06 and M15. Converts adaptive physical operations into the algebraic object required by the converse.
- **Conceptual connection:** Feedback can correlate the observed records, yet each fixed branch still has a product effect on the independent input copies. The proof does not assume independent recorded transcripts.
- **Source pointers:** Watrous [§§2.1.2, 2.3.2][W2]; project [binary Lemma 1](../science/binary-sample-law.md#lemma-1-product-effects-for-a-complete-recorded-transcript).

### M17 — Normalized hybrids and relative-entropy accumulation

- **Central question:** How can one charge statistical information once per copy despite arbitrary interleaving?
- **Understanding target:** Construct the physical hybrid run that replaces only copy $`i`$ by the maximally mixed state while leaving the same protocol in place. Explain the likelihood-product identity and why the resulting relative entropies sum exactly and are bounded by $`N\delta_n^2`$.
- **Dependencies and story role:** Uses M08 and M16. Supplies the central adaptive information bound.
- **Conceptual connection:** Each hybrid is a normalized probability law, so its likelihood has mean one. That fact turns uniform branch closeness into a quadratic information bound with no extra penalty for interleaving.
- **Source pointers:** Watrous [§§5.1.1–5.1.2][W5]; project [binary Lemma 2](../science/binary-sample-law.md#lemma-2-hybrid-relative-entropy-identity).

### M18 — The converse for every permitted decision rule

- **Central question:** Why must a reliable final decision consume enough copies to overcome the small transcript information?
- **Understanding target:** Combine the two conditional-error requirements with classical coarse-graining and the hybrid bound to obtain the finite-copy converse. Explain why it covers target-dependent randomization, bounded stopping and discarded records, and why it does not require the finite-size deviation to be below one.
- **Dependencies and story role:** Uses M07 and M17. Completes the lower-bound branch of the binary argument.
- **Conceptual connection:** A successful final bit must retain a fixed amount of statistical separation. No classical decision rule can create that separation from an insufficiently informative full transcript.
- **Source pointers:** Watrous [§3.1.1][W3] and [§5.1.2][W5]; project [binary Theorem 3](../science/binary-sample-law.md#theorem-3-finite-dimensional-converse).

### M19 — The signal left in a fixed basis

- **Central question:** What usable information survives when every copy is measured in the same computational basis?
- **Understanding target:** Explain the noisy probability distribution as a bit-flip convolution and express its correlations using parity characters. Understand why a correlation on a subset of sites is attenuated by a power of $`s`$, and why the squared residual correlations sum to chi-square divergence from uniform.
- **Dependencies and story role:** Uses M03, M04 and M08. Starts the achievable-test branch with a concrete permitted measurement.
- **Conceptual connection:** The same detector contraction that smooths every local effect also determines the remaining classical signal in a simple fixed measurement.
- **Source pointers:** Watrous [§1.1.2][W1] and [§2.3.1][W2] for the operator framework; project [binary §3, through Eq. (16)](../science/binary-sample-law.md#3-fixed-basis-statistics-and-exact-haar-moments) for the parity calculation.

### M20 — From an average collision scale to typical signal

- **Central question:** Why does a typical target retain enough fixed-basis signal, rather than merely a nonzero ensemble average?
- **Understanding target:** Identify the roles of the second and fourth Haar moments in the exact mean and variance of chi-square divergence. Explain how, at fixed $`0\lt q\lt 1/2`$, the relative-variance bound shows that the signal has scale $`b^n`$ with high target probability.
- **Dependencies and story role:** Uses M10 and M19. Establishes the typical lower bound on signal needed for achievability.
- **Conceptual connection:** An average signal alone could be dominated by rare targets. The fourth-moment calculation controls that possibility and complements the uniform upper control on individual likelihood deviations.
- **Source pointers:** Watrous [§§7.1.1, 7.2.1, Lemma 7.24][W7]; project [binary Lemma 4 and its consequences](../science/binary-sample-law.md#3-fixed-basis-statistics-and-exact-haar-moments), with [collision-scale attribution](../references/RELATED_WORK.md#2-fixed-noisy-measurements-already-exhibit-the-same-collision-scale).

### M21 — A likelihood test at the reciprocal signal scale

- **Central question:** How does surviving chi-square signal become a test with both errors controlled?
- **Understanding target:** Use the uniform likelihood bound to compare chi-square divergence with squared Hellinger distance. Explain affinity multiplication across independent fixed-basis records and the error guarantee of the known-distribution likelihood test, while retaining the possible exponential classical evaluation cost.
- **Dependencies and story role:** Uses M08, M14 and M20. Converts the moment calculation into an attainable copy bound.
- **Conceptual connection:** Uniform regularity and a lower bound on total signal do different jobs; together they justify a sample cost proportional to the inverse signal.
- **Source pointers:** Watrous [§3.2][W3] for the fidelity/affinity connection; project [binary Lemma 5 and Proposition 6](../science/binary-sample-law.md#4-from-chi-square-divergence-to-a-test-with-controlled-errors).

### M22 — The optimal binary exponential rate

- **Central question:** What exactly matches when the converse and the fixed-basis test are combined?
- **Understanding target:** Derive the rate $`-\log b`$ at fixed $`0\lt q\lt 1/2`$ from the two bounds on their common typical-target event. Distinguish the matched exponential rate from the unmatched polynomial prefactor, and explain why the noiseless and fully random-report endpoints require separate statements.
- **Dependencies and story role:** Integrates M13–M21 around the binary task specified in M12.
- **Conceptual connection:** A highly adaptive strategy and a fixed basis have the same leading exponential copy cost in this model. This conclusion is limited to the binary promise and does not identify a full-fidelity exponent.
- **Source pointers:** Watrous [§3.1.1][W3] and [§7.2.1][W7]; project [binary Theorem 7](../science/binary-sample-law.md#theorem-7-binary-sample-law) and [§6](../science/binary-sample-law.md#6-endpoints-and-certification-scope).

### M23 — An observable that separates fidelity promises

- **Central question:** What extra structure provides soundness against every low-fidelity alternative?
- **Understanding target:** Explain Du et al.'s target-dependent verification observable, its target eigenvector and its spectral gap. Relate this gap to separated good and bad fidelity expectations, and explain how the nonadaptive local-Pauli score measures that observable without outcome-dependent physical bases.
- **Dependencies and story role:** Uses M09, M10 and M12. Introduces the research ingredient that the binary upper bound does not supply.
- **Conceptual connection:** A witness inequality converts one observable's expectation into a statement uniform over a composite class of input states; a constant Haar-typical gap is a separate theorem.
- **Source pointers:** Watrous [§1.1.3][W1], [§2.3.1][W2] and [§3.2][W3]; project [fidelity §§2–3](../science/fidelity-certification.md#2-the-target-dependent-verification-observable), including the precise Du attribution.

### M24 — Classical detector inversion and its statistical cost

- **Central question:** How can an unbiased verification score be recovered from noisy reports, and what price does the correction pay?
- **Understanding target:** Explain inverse-channel weights as classical signed estimator coefficients rather than physical inverse probabilities. Connect the product inverse's row norm to score-range growth, and then to a finite-sample guarantee with the required positive fidelity-promise gap.
- **Dependencies and story role:** Uses M03, M08 and M23. Supplies a concrete sufficient protocol for noisy fidelity certification.
- **Conceptual connection:** Exact unbiasedness does not imply low variance or low copy cost. Nonadaptive basis choice makes the fixed classical channel inversion valid; the calculation does not automatically extend to feedback-dependent bases.
- **Source pointers:** Watrous [§1.1.2][W1] and [§2.2.1][W2] for linear maps; project [fidelity §§4–5](../science/fidelity-certification.md#4-exact-classical-inversion-of-the-detector-channel).

### M25 — The polynomial-copy fidelity threshold

- **Central question:** How accurately must each detector report be acquired as the number of qubits grows?
- **Understanding target:** Embed the maximally mixed state in the bad-fidelity set and combine that necessity with the corrected-score construction. Interpret the criterion $`nq_n=O(\log n)`$, its robust gap-dependent promise, and the distinction between a divergent noise-budget ratio and an unbounded oscillating ratio.
- **Dependencies and story role:** Uses M18 and M24. Integrates the fidelity branch while keeping it separate from binary achievability.
- **Conceptual connection:** Different lower and upper exponential factors can still determine the same polynomial-versus-superpolynomial threshold. They do not establish an optimal fixed-noise exponent for composite certification.
- **Source pointers:** Watrous [§§3.1.1, 3.2][W3] for task foundations; project [fidelity §§6–8](../science/fidelity-certification.md#6-necessity-from-the-target-informed-binary-converse).

### M26 — Transferring the binary law through finite moments

- **Central question:** Which properties of Haar randomness are actually needed by the proof?
- **Understanding target:** Define an approximate state design through its additive trace-norm moment error. Explain why high enough moment order and sufficiently small error transfer both the uniform event and the fixed-basis signal, including the dimension-dependent amplification of approximation error.
- **Dependencies and story role:** Uses M10, M14, M20 and M22. Extends the binary argument to a specified family of non-Haar target ensembles.
- **Conceptual connection:** The proof uses a finite set of controlled moments, not every feature of Haar measure. Matching those moments is sufficient only at the explicitly charged accuracy and does not transfer the full-fidelity spectral gap automatically.
- **Source pointers:** Watrous [§1.1.3][W1] and [§§7.1.1, 7.2.1][W7]; project [circuit targets §§1–3](../science/circuit-targets.md#1-moment-convention-and-result) and [§6](../science/circuit-targets.md#6-scope-of-the-transfer).

### M27 — Preparation circuits and supplied coherent inversion

- **Central question:** Can the hard targets have polynomial preparation circuits, and what changes if those circuits may be inverted before detection?
- **Understanding target:** Connect the required design parameters to the cited finite-gate construction and its precision budget. Compare unlimited classical use of the supplied circuit description with paying for its coherent inverse, which creates a constant-gap one-bit binary test before reporting noise.
- **Dependencies and story role:** Uses M06, M07 and M26. Separates preparation cost, classical advice and coherent measurement capabilities.
- **Conceptual connection:** A polynomial preparation description does not imply efficient classical likelihood evaluation or shallow preparation. The inverse comparison supplies the same target information to both strategies and explicitly charges the extra coherent gates.
- **Source pointers:** Watrous [§2.2.3][W2] for unitary channels; project [circuit targets §§4–6](../science/circuit-targets.md#4-a-polynomial-preparation-construction-and-its-precision), including the BHH construction and inverse-preparation attribution.

### M28 — Acquisition noise, separable effects and surviving global information

- **Central question:** Can the quantum information remain globally distinguishable while every allowed local acquisition is expensive?
- **Understanding target:** Explain the one-use statistical equivalence between detector bit flips and local depolarization before measurement. Extend the uniform effect bound to arbitrary one-copy separable POVMs, and compare it with the global typical-error-span test under its explicit entropy condition.
- **Dependencies and story role:** Uses M15, M18 and M22. Places the local copy law inside a wider measurement-class comparison.
- **Conceptual connection:** Separable acquisition restricts how information can be extracted, not necessarily how much global state distinguishability remains. The global projector has no claimed efficient implementation, and its sufficient entropy regime is not a sharp transition theorem.
- **Source pointers:** Watrous [§2.2.3][W2], [§§6.1.1, 6.1.3][W6] and [§5.3.1][W5]; project [acquisition §§1–3](../science/acquisition-and-control.md#1-two-explicitly-located-noise-models), including the copywise restriction and prior context.

### M29 — Redundant acquisition and the location of irreversible noise

- **Central question:** Which added local resources can restore reliable reports, and why do they change the experiment?
- **Understanding target:** Explain majority decoding of repeated ideal nondemolition reports and its local-ancilla realization for a chosen measurement basis. Account for reports, clean ancillas and gates, distinguish copied basis outcomes from arbitrary-state cloning, and explain why redundancy after an acquisition layer does not undo that layer.
- **Dependencies and story role:** Uses M03, M06, M24 and M28. Completes the physical-resource comparisons with local alternatives to coherent global processing.
- **Conceptual connection:** The order of encoding, irreversible noise and detection determines what information redundancy can protect. Independent repetition errors are a load-bearing assumption.
- **Source pointers:** Watrous [§§2.2.1–2.2.3][W2] and [§1.2.2][W1]; project [acquisition §§4–7](../science/acquisition-and-control.md#4-repeated-qnd-reports).

### M30 — The complete scientific account and its boundaries

- **Central question:** What does the project establish about known-state testing, and which conclusions require different evidence or resources?
- **Understanding target:** Connect the uniform theorem, adaptive converse, matching binary test, fidelity noise budget, design transfer and acquisition comparisons into one account. Identify the hypotheses and evidence behind each claim, separate inherited ingredients from the operational addition, and distinguish analytical proof from finite numerical checks.
- **Dependencies and story role:** Integrates M12, M22 and M25–M29; completes the narrative phase without introducing another result or task.
- **Conceptual connection:** Complete target knowledge, ideal local capability and global distinguishability can coexist with exponential noisy local copy cost. The explanation is the specified one-report acquisition architecture, with its target, noise, resource and quantifier assumptions retained.
- **Source pointers:** Watrous [Chapters 2][W2], [3][W3] and [7][W7] for the common framework; project [model §§3–5](../science/model-and-results.md#3-result-map), [related work](../references/RELATED_WORK.md), [resource summary](../science/acquisition-and-control.md#7-resource-summary) and [finite-check scope](../code/README.md#analytical-claims-and-numerical-limits).

## Canonical reading routes

The [science index](../science/README.md) gives the proof dependency order. The [Watrous bridge](WATROUS_BRIDGE.md) supplies selected textbook readings and notation translations. The [structured references](../references/REFERENCES.md) identify imported research theorems. These routes support the same thirty targets while leaving the full technical argument in its authoritative science pages.

[Watrous]: https://cs.uwaterloo.ca/~watrous/TQI/
[WContents]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf
[W1]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf
[W2]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf
[W3]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf
[W5]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf
[W6]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf
[W7]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf
