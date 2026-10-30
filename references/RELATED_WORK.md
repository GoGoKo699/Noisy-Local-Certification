# Relation to existing work

The contribution is the optimal exponential sample rate for a fully known generic target under one destructive noisy local report per qubit, including target-informed measurement choices and arbitrary classical feedback. The collision factor, high-moment methods, circuit designs and broad noisy data-hiding mechanism have antecedents. This comparison separates those ingredients from the operational statement proved here.

## 1. Ideal local certification supplies the capability being tested

[Du et al.](REFERENCES.md#du) show that ideal local Pauli measurements give a constant verification gap for Haar-typical targets. Their fidelity protocol supplies a bounded score and constant-copy performance at fixed suitable tolerances. Their robustness concerns prepared-state deviations, not independent errors in reported outcomes. This repository changes the reporting model and derives both a converse and an explicit corrected-score protocol.

The general-fidelity statement is correspondingly precise: exact-target completeness is covered, and a robust good-state neighborhood is allowed when the ideal gap separates the good and bad promises. The exact fixed-noise exponential rate is established only for the binary target-versus-maximally-mixed problem.

## 2. Fixed noisy measurements already exhibit the same collision scale

[Maciejewski, Puchała and Oszmaniec](REFERENCES.md#average-case-distances) analyze generic experiments through average-case distances. Their fixed noisy product measurement has an explicit collision expression involving the product of $1-2q_i(1-q_i)$. For homogeneous errors this is the $b^n$ scale used here. Their work also studies pure-target versus maximally-mixed discrimination with other measurement resources.

The additional quantifier required here is simultaneous control after the target is given. A fixed-measurement Haar average leaves open whether each known target admits a better local measurement. The [uniform theorem](../science/uniform-concentration.md) controls every noisy product effect on one target event. The [transcript argument](../science/binary-sample-law.md) then includes all permitted classical adaptation, including measurements interleaved across copies. The fourth-moment calculation supplies a matching fixed-basis exponential rate. The collision factor itself is not presented as a new mechanism.

## 3. An ensemble-universal measurement differs from a target-informed one

[Liu et al.](REFERENCES.md#scrambling-under-noise) study distinguishability of noisy design ensembles. Their Section IV distinguishes measurements tailored to a pair from a single measurement applied to every member of an unknown ensemble. Their local data-hiding application limits an observer to a subsystem and discards its complement.

The verifier here receives the target description and can select its measurement accordingly. It can collect one report from every input site, with unrestricted classical feedback. These are different access and quantifier conventions. The comparison must use the full statements, rather than interpret an abstract's phrase about any measurement as permitting target information that the theorem does not supply.

Global survival under noise and the entropy threshold are inherited context. The elementary typical-error-span projector in [acquisition and control](../science/acquisition-and-control.md) gives a transparent target-versus-mixed comparison. Its role is to identify the acquisition resource responsible for the local copy cost; the global survival mechanism is not a separate originality claim.

## 4. Concentration and preparation methods are established tools

[Low](REFERENCES.md#design-concentration) gives high-moment transfer principles and product-state net arguments. [Brandão, Harrow and Horodecki](REFERENCES.md#circuit-designs) give polynomial-size approximate-design circuits and related indistinguishability results against restricted coherent circuits.

The analysis here uses that methodological lineage. It requires exponentially small relative deviations of centered noisy product effects, then translates those deviations into a full adaptive sample bound. The [circuit extension](../science/circuit-targets.md) accounts for the design order and moment error needed by this proof. The allowed classical postprocessing is unbounded, so a result that restricts the entire readout circuit size does not directly supply the present statement.

## 5. Structured verification and noisy data hiding

[Zhang et al.](REFERENCES.md#noisy-verification-strategies) treat noisy prescribed verification operators, including structured entangled targets and symmetric bit-flip readout. Parity attenuation, a reduced verification gap and noise-aware testing are already established phenomena. Their analyzed strategies do not optimize over every permitted local protocol for a generic fully known target.

[Lupo, Wilde and Lloyd](REFERENCES.md#noisy-data-hiding) establish noisy-channel data-hiding results using randomized mixed codewords. Concentration, nets and security against separable measurements are part of that context. The source states, task and resource scaling here are instead a single known pure target against the maximally mixed state, with an optimized number of independently prepared copies.

## Scope of the established addition

The scientific content consists of a uniform target-informed converse, the matching binary exponential rate, a properly scoped full-fidelity noise budget, and explicit preparation/acquisition resource accounting. Its boundaries remain visible: generic rather than every target, one report per qubit, independent calibrated detector noise, sample rather than classical runtime complexity, and no free coherent readout or redundancy. The accompanying proofs establish these statements at their declared scope; the reference comparison does not claim exhaustive coverage of every possible formulation in the literature.
