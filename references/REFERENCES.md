# Primary references

Source versions below identify the statements used in the scientific account. Equations and proofs developed in this repository are written independently; the cited works own the imported results and methods identified here.

## Du

Zhenyu Du, Jinchang Liu, Elias X. Huber, Zi-Wen Liu and Xiongfeng Ma, **Certifying localizable quantum properties with constant sample complexity**, Physical Review X **16**, 041027 (2026). [arXiv:2509.17580v3](https://arxiv.org/html/2509.17580v3), 20 July 2026; [published article](https://journals.aps.org/prx/abstract/10.1103/rkl6-hfrn).

Used locations: Section VII, Eq. (33), Theorem 5, Appendix A Eq. (A2), and Appendix F.1. These supply the ideal conditional-fidelity observable, its Haar-typical constant gap and the bounded local-shadow score. The present detector-channel inversion is derived in [fidelity certification](../science/fidelity-certification.md).

## Average-case distances

Filip B. Maciejewski, Zbigniew Puchała and Michał Oszmaniec, **Operational Quantum Average-Case Distances**, Quantum **7**, 1106 (2023). [Version of record and bibliographic data](https://quantum-journal.org/papers/q-2023-09-11-1106/); [full paper](https://quantum-journal.org/papers/q-2023-09-11-1106/pdf/); [arXiv:2112.14283v5](https://arxiv.org/abs/2112.14283v5).

The same authors, **Exploring Quantum Average-Case Distances: proofs, properties, and examples**, [arXiv:2112.14284v6](https://arxiv.org/html/2112.14284v6), 1 March 2023.

Used locations: the operational paper's Theorem 2 and Examples 2 and 6; companion Example 10, Eq. (132). The fixed noisy-product collision factor and average readout suppression are inherited. The exact companion formula is used instead of relying on a simplified exponential estimate.

## Scrambling under noise

Guoding Liu, Chushi Qin, Zitai Xu, Xiongfeng Ma and Zi-Wen Liu, **Can scrambling protect quantum state distinguishability under noise?**, [arXiv:2606.02122v1](https://arxiv.org/abs/2606.02122), 1 June 2026. This is a preprint. [Author-institution record](https://quics.umd.edu/publications/can-scrambling-protect-quantum-state-distinguishability-under-noise); [public copy of the primary manuscript](https://www.researchgate.net/publication/405682986_Can_scrambling_protect_quantum_state_distinguishability_under_noise).

Used locations: the noisy-ensemble distinguishability results, Section IV's explicit distinction between pair-dependent and ensemble-universal measurements, and the local data-hiding discussion. Global information survival and the entropy-threshold context are prior results. The [related-work comparison](RELATED_WORK.md) states the different measurement quantifiers.

## Design concentration

Richard A. Low, **Large Deviation Bounds for k-designs**, [arXiv:0903.5236](https://arxiv.org/pdf/0903.5236) (2009).

Used locations: Theorem 1.2, transferring high moments, and Theorem 6.4, using a product-state net for uniform overlap control. These methods are antecedents of the proof architecture; the centered noisy-effect concentration estimate is proved in full in [uniform concentration](../science/uniform-concentration.md).

## Circuit designs

Fernando G. S. L. Brandão, Aram W. Harrow and Michał Horodecki, **Local random quantum circuits are approximate polynomial-designs**, Communications in Mathematical Physics **346**, 397–434 (2016). [Corrected arXiv:1208.0692v4](https://arxiv.org/pdf/1208.0692v4); [DOI](https://doi.org/10.1007/s00220-016-2706-8).

Used locations: Definition 2, Lemma 3 and Corollaries 6–7 for the design convention and polynomial circuit construction; Corollary 10 for related restricted-circuit indistinguishability. The exact state-moment accuracy required here and its cost are derived in [circuit targets](../science/circuit-targets.md).

## Noisy verification strategies

Lan Zhang, Yinfei Li, Ye-Chao Liu and Jiangwei Shang, **Verification of entangled states under noisy measurements**, Advanced Quantum Technologies (2025). [arXiv:2406.01470v2](https://arxiv.org/html/2406.01470v2), 20 February 2025.

Used locations: Sections 3 and 5, including the symmetric independent readout model and prescribed GHZ/stabilizer verification strategies. This is a source for existing noise-aware verification analysis, rather than the optimized generic-target converse.

## Noisy data hiding

Cosmo Lupo, Mark M. Wilde and Seth Lloyd, **Quantum data hiding in the presence of noise**, IEEE Transactions on Information Theory **62**, 3745–3756 (2016). [arXiv:1507.06038v2](https://arxiv.org/html/1507.06038v2).

Used locations: Theorem 3, the randomized mixed-codeword construction and Appendices B–C on concentration and separable measurements. Noisy data hiding is established context; the present fixed known pure target and binary copy rate are distinguished in the comparison.

## Foundational reading

John Watrous, **The Theory of Quantum Information**, Cambridge University Press (2018). [Author's book and chapter page](https://cs.uwaterloo.ca/~watrous/TQI/). Chapters 2–3 cover states, measurements and distinguishability; Chapter 7 develops permutation invariance and Haar measures. The author's hosted manuscript is for personal use and is linked, not redistributed here.
