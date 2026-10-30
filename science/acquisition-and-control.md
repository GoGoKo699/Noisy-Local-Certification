# Acquisition noise and coherent control

There are two useful operational readings of the noisy local test. The original architecture has a clean projective measurement followed by a corrupted classical report. A second architecture applies a local depolarization layer before the verifier acquires the quantum system. They produce the same statistics for a single projective measurement of each qubit, including local classical feedforward. They are different when repeated measurements, redundant encoding, or entangling control are introduced.

This distinction determines which additional resources restore efficient testing.

## 1. Two explicitly located noise models

Let $d=2^n$, $\tau=I/d$, $s=1-2q$, and $0<q<1/2$. Define the single-qubit channel, also on unnormalized operators, by

$$
\mathcal D_q(X)=sX+q\,\operatorname{tr}(X)I.
\tag{1}
$$

It is trace preserving, unital, self-adjoint in the Hilbert–Schmidt inner product, and multiplies Bloch vectors by $s$.

| Feature | Detector reports | Acquisition layer |
|---|---|---|
| Location of noise | After a clean local projective measurement | Before any accessible quantum processing |
| Supplied object | An independent copy of $\rho$ | An independent copy of $\mathcal D_q^{\otimes n}(\rho)$ |
| Basic local observation | One projective measurement per input qubit, then a BSC$(q)$ report | Any one-copy separable POVM, with ideal outcome recording |
| Across copies | Classical memory and the adaptation specified in the main model | Classical adaptation between copywise POVMs |
| Quantum resources excluded from the stated converse | Repeated reports and redundant encoding before the single detector use; coherent coupling of input sites or copies | Joint measurements with entangled effects across sites, or coherent processing joining different source copies |

In the acquisition model the channel environment is unavailable. No measurement outcome or redundant encoding can be retained from before the acquisition layer. Local ancillas introduced afterwards are permitted when their resulting measurement on the supplied input has separable effects.

The acquisition result below is stated for **copywise separable measurements**. It does not assert a bound for a joint many-copy separable measurement whose local factors act on quantum memories containing several source copies.

### Exact equivalence for one use of each local detector

A clean projective measurement along a unit Bloch vector $u$ has effects

$$
P_\pm(u)=\frac{I\pm u\cdot\sigma}{2}.
$$

If its reported sign is independently flipped with probability $q$, the reported effect is

$$
F_\pm(u)
=(1-q)P_\pm(u)+qP_\mp(u)
=\frac{I\pm s\,u\cdot\sigma}{2}
=\mathcal D_q^\dagger(P_\pm(u)).
\tag{2}
$$

For an adaptive local protocol, fix its random seed and its complete reported path $y$. Every axis and the order of measured sites are then fixed along that path. Summing the hidden ideal outcomes with their BSC probabilities produces a tensor product of the effects in (2), one per site. The same tensor product is obtained by applying $\mathcal D_q^{\otimes n}$ first and then executing the corresponding clean projective protocol with its observed outcomes as the feedback record.

If some sites are not measured, the physical effect has identity factors at those sites. After dividing by its trace, these become $I/2$. Thus partial records are covered by normalized products of the form

$$
E=\bigotimes_{j=1}^n
\frac{I+s\,u_j\cdot\sigma}{2},
\qquad |u_j|\le1.
\tag{3}
$$

The equivalence is an equality of the outcome laws for this one-use architecture. It does not identify the two physical instruments for future measurements of the same qubit. Repeating a noisy classical report after a clean nondemolition projection is therefore not modeled by applying (1) once and receiving an ideal measurement record.

## 2. Extension to every one-copy separable POVM

Suppose a target $\psi$ satisfies the uniform event

$$
\left|d\,\operatorname{tr}(\psi E)-1\right|
\le\delta
\quad\text{for every product }E\text{ in (3)}.
\tag{4}
$$

[Uniform concentration](uniform-concentration.md) establishes (4) for Haar-typical targets, with

$$
\delta=\delta_n
=1024\left[n b^{n/2}+n^2a^n\right],
\qquad
a=1-q,\quad b=a^2+q^2.
\tag{5}
$$

[Polynomial circuit targets](circuit-targets.md) establishes the corresponding event for the specified approximate-design ensembles.

**Proposition 1 — separable effects after acquisition.** Let $\{M_y\}_y$ be any one-copy separable POVM, chosen with arbitrary dependence on the known target. If (4) holds, then for every outcome with nonzero probability under $\tau$,

$$
1-\delta
\le
\frac{\operatorname{tr}[M_y\mathcal D_q^{\otimes n}(\psi)]}
{\operatorname{tr}(M_y\tau)}
\le1+\delta.
\tag{6}
$$

**Proof.** A nonzero separable positive effect has a finite decomposition

$$
M_y=\sum_k\bigotimes_{j=1}^n F_{ykj},
\qquad F_{ykj}\ge0.
\tag{7}
$$

Terms containing a zero-trace factor are zero and can be dropped. For every remaining local factor write

$$
F_{ykj}=f_{ykj}\,\omega_{ykj},
\qquad
f_{ykj}=\operatorname{tr}F_{ykj}>0,\qquad
\omega_{ykj}=\frac{I+r_{ykj}\cdot\sigma}{2},
\quad |r_{ykj}|\le1.
$$

Its adjoint-noisy image is

$$
\mathcal D_q^\dagger(F_{ykj})
=f_{ykj}\frac{I+s\,r_{ykj}\cdot\sigma}{2}.
$$

Consequently,

$$
\frac{(\mathcal D_q^\dagger)^{\otimes n}(M_y)}
{\operatorname{tr}M_y}
=\sum_k w_{yk} E_{yk},
\qquad
w_{yk}=
\frac{\prod_j f_{ykj}}{\operatorname{tr}M_y},
\qquad
\sum_k w_{yk}=1,
\tag{8}
$$

where each $E_{yk}$ has the form (3). Trace preservation gives the normalization, and positivity gives $w_{yk}\ge0$. Since $\mathcal D_q^{\otimes n}(\tau)=\tau$, the likelihood ratio in (6) is exactly

$$
d\sum_k w_{yk}\operatorname{tr}(\psi E_{yk}).
$$

Equation (4) and convexity prove (6). An effect of zero probability under $\tau$ is the zero operator, so it also has zero probability under the noisy target. $\square$

No bound on the number of POVM outcomes or the number of product terms was used. For continuous outcome spaces, the same inequalities hold for every measurable coarse-grained effect and hence for the likelihood-ratio density. The argument covers separable measurements beyond those implementable by local operations and classical communication.

### Copy complexity

Let $P$ and $Q$ be the single-copy record laws under the noisy target and under $\tau$. Equation (6) implies

$$
\chi^2(P\|Q)
=\mathbb E_Q\left(\frac{dP}{dQ}-1\right)^2
\le\delta_n^2,
\qquad
D(P\|Q)\le\delta_n^2.
\tag{9}
$$

This remains true conditional on any preceding classical record, because (4) is uniform over the next target-dependent POVM. For $N$ independent copies processed by such copywise POVMs, the relative-entropy chain rule gives

$$
D(P^{(N)}\|Q^{(N)})\le N\delta_n^2.
\tag{10}
$$

Both errors at most $1/3$ require $N\delta_n^2\ge2/9$. Thus for fixed $q$,

$$
N\ge c_q\,n^{-2}b^{-n}.
\tag{11}
$$

The computational-basis measurement after acquisition has exactly the BSC outcome law used by the matching test in [Binary sample law](binary-sample-law.md). Its upper bound also applies here. Hence the same exponent $-\log b$ is optimal even among these arbitrary copywise separable POVMs.

The restriction on copies matters. A product effect across the $n$ physical sites of one copy is covered by (4). An effect whose local factors jointly act on multiple source copies has a different local Hilbert space and is not covered by this proof.

## 3. A one-copy global test after the same acquisition noise

The local limitation does not imply that the acquired quantum states are themselves close in trace distance. There is a regime where they are nearly perfectly distinguishable by a global measurement.

Write (1) as the Pauli channel

$$
\mathcal D_q(\rho)
=p_0\rho+p_1X\rho X+p_2Y\rho Y+p_3Z\rho Z,
$$

with

$$
p_0=1-\frac{3q}{2},\qquad
p_1=p_2=p_3=\frac q2.
\tag{12}
$$

Let

$$
h(q)=H_4(p)
=-\sum_{\ell=0}^3p_\ell\log_2p_\ell.
\tag{13}
$$

**Proposition 2 — a typical-error-span test.** Fix $q$ with $h(q)<1$, and choose $0<\xi<1-h(q)$. For every known pure target $\psi$ there is a two-outcome global POVM on one acquired copy whose false-rejection and false-acceptance probabilities satisfy

$$
\begin{aligned}
\alpha_n
&\le
\exp\!\left[-\frac{2n\xi^2}{R(q)^2}\right],\\
\beta_n
&\le 2^{-n[1-h(q)-\xi]},
\qquad
R(q)=\log_2\frac{1-3q/2}{q/2}.
\end{aligned}
\tag{14}
$$

The hypotheses are $\mathcal D_q^{\otimes n}(\psi)$ and $\tau$. Haar randomness is not assumed in this proposition.

**Proof.** A Pauli error string is $e=(e_1,\ldots,e_n)\in\{0,1,2,3\}^n$, with probability
$p_e=\prod_jp_{e_j}$ and corresponding Pauli operator $P_e$. Define the one-sided information-typical set

$$
T_{n,\xi}
=
\left\{
e:-\frac1n\log_2p_e\le h(q)+\xi
\right\}.
\tag{15}
$$

This set depends on the channel and on $n,\xi$, not on the target.
Every string in it has probability at least $2^{-n[h(q)+\xi]}$, so

$$
|T_{n,\xi}|\le2^{n[h(q)+\xi]}.
\tag{16}
$$

For independent errors, the variables $-\log_2p_{e_j}$ have mean $h(q)$ and range of length $R(q)$. Hoeffding's inequality gives

$$
\sum_{e\notin T_{n,\xi}}p_e
\le\exp\!\left[-\frac{2n\xi^2}{R(q)^2}\right].
\tag{17}
$$

Let $\Pi_\psi$ be the orthogonal projector onto

$$
\mathcal V_\psi
=
\operatorname{span}
\{P_e|\psi\rangle:e\in T_{n,\xi}\}.
\tag{18}
$$

The vectors in (18) need not be orthogonal or linearly independent. For every included error, its entire state lies in the span. Therefore

$$
\begin{aligned}
\operatorname{tr}\!\left[
\Pi_\psi\mathcal D_q^{\otimes n}(\psi)
\right]
&=\sum_e p_e
\langle\psi|P_e^\dagger\Pi_\psi P_e|\psi\rangle\\
&\ge\sum_{e\in T_{n,\xi}}p_e.
\end{aligned}
\tag{19}
$$

Under the maximally mixed hypothesis,

$$
\operatorname{tr}(\Pi_\psi\tau)
=\frac{\dim\mathcal V_\psi}{2^n}
\le\frac{|T_{n,\xi}|}{2^n}
\le2^{-n[1-h(q)-\xi]}.
\tag{20}
$$

Accepting the target on outcome $\Pi_\psi$ proves (14). $\square$

Taking $\xi=[1-h(q)]/2$ makes both errors exponentially small. In particular,

$$
\frac12\left\|
\mathcal D_q^{\otimes n}(\psi)-\tau
\right\|_1
\ge1-\alpha_n-\beta_n
=1-e^{-\Omega_q(n)}.
\tag{21}
$$

The equation $h(q)=1$ has the unique solution in $(0,1/2)$

$$
q_*=0.12619308327682116\ldots.
\tag{22}
$$

Indeed, $h'(q)=\tfrac32\log_2[(1-3q/2)/(q/2)]>0$ on this interval. In the alternative convention
$\mathcal D(\rho)=(1-p)\rho+pI/2$, the sufficient range is
$p=2q<0.2523861665536423\ldots$.

This is a sufficient entropy condition for the displayed test, not a proof of a sharp global distinguishability threshold. The projector is an information-theoretic measurement; no polynomial-size implementation is claimed. In particular, supplying a polynomial preparation circuit for $\psi$ does not by itself make the span projector in (18) efficient.

### Consequence and prior context

For every fixed $0<q<q_*$ and a typical target in the proved ensembles, the same acquired pair has a one-copy global test with vanishing error, while arbitrary copywise separable tests require $b^{-n+o(n)}$ copies. For Haar targets, ideal local measurements before acquisition noise also have constant-copy certification protocols; their relevant scope is stated in [Fidelity certification](fidelity-certification.md).

Noisy data hiding and noise-resilient global distinguishability have established precedents. Lupo, Wilde, and Lloyd [develop noisy data-hiding capacities](https://arxiv.org/pdf/1507.06038). Liu et al. [identify the same channel-entropy regime for global distinguishability of scrambled ensembles](https://arxiv.org/abs/2606.02122). Their fixed-universal-measurement result and subsystem-access application have different quantifiers from the all-sites, known-target separable bound above. The present global construction uses standard typical-error counting; the operational conjunction with the optimized local copy law is the relevant comparison. See [Related work](../references/RELATED_WORK.md).

## 4. Repeated QND reports

In the detector-report model, suppose an ideal nondemolition measurement can be repeated in the same chosen basis. The first ideal projection fixes a measurement eigenvalue $x$. Every later clean measurement returns that same $x$, while each classical report is independently corrupted with probability $q$.

For an odd number $r$ of reports, majority decoding has effective error

$$
q_r=
\sum_{k=(r+1)/2}^r
\binom rk q^k(1-q)^{r-k}
\le
\exp[-2r(1/2-q)^2]
=e^{-rs^2/2}.
\tag{23}
$$

Consider an ideal protocol in the one-use local model, using at most $T_0$ source copies and hence at most $nT_0$ ideal outcome bits. Couple it to a protocol using these repeated reports and the same random choices. Until the first incorrectly decoded bit, their adaptive measurement choices agree. A union bound gives a discrepancy probability at most $nT_0q_r$. Thus

$$
r\ge\frac{2}{s^2}\log\frac{nT_0}{\eta},
\tag{24}
$$

rounded up to an odd integer, makes the final transcript distributions differ in total variation by at most $\eta$.

For fixed $q$, a constant-copy ideal protocol can therefore be recovered to fixed accuracy using $O_q(\log n)$ reports per qubit and $O_q(n\log n)$ total detector reports per source copy. This changes the one-use resource model. It also requires independent reporting errors across repetitions; a persistent calibration error is not reduced by this argument.

In the acquisition model, repeating an ideal measurement after (1) does not reconstruct the pre-channel state. Such local operations are already included in the separable-effect proposition. The equality of one-use statistics in (2) does not extend to the QND repetition experiment.

## 5. Local ancilla repetition before the detectors

The same repetition code can be implemented in the detector model by coherent local redundancy. Rotate the chosen measurement basis to the computational basis, append $r-1$ clean local ancillas in $|0\rangle$, and apply $r-1$ CNOT gates from the input qubit to those ancillas. Measuring all $r$ qubits in the computational basis gives repeated copies of the chosen measurement eigenvalue, followed by $r$ independent BSC reports. Majority decoding again has error (23).

This construction copies a chosen basis outcome. It is not a map that clones an arbitrary unknown qubit state. Applied independently at each site, it reproduces the desired joint distribution of local projective outcomes, including when the input sites are entangled.

For $n$ sites and repetition factor $r$, the additional resources per source copy are

- $n(r-1)$ clean ancillas;
- $n(r-1)$ ideal CNOT gates within the local sites;
- $nr$ destructive detector uses, together with the chosen basis rotations.

With $r=O_q(\log n)$, these resources restore a constant-copy ideal local test by the same coupling argument as (24). Gate faults, ancilla faults, and correlated detector errors would require their own error analysis.

Ancillas introduced only after an acquisition layer do not evade Proposition 1 when all processing is local: the induced POVM on the original noisy input still has separable effects. Encoding into redundant carriers before the acquisition layer changes both the supplied system and the location or number of noisy channels, and is a separately charged architecture.

## 6. Coherent inverse preparation before readout

If a known target is prepared by a supplied $G$-gate circuit $U$, an ideal coherent inverse before the detectors converts the binary promise into

$$
|0^n\rangle\langle0^n|\quad\text{versus}\quad I/2^n.
$$

A single reported computational-basis bit then has probabilities $1-q$ and $1/2$ under the two hypotheses. The gap $(1-2q)/2$ is independent of $n$, so $O_q(1)$ copies suffice at constant error. The precise test, gate count, and inverse-precision budget are given in [Polynomial circuit targets](circuit-targets.md).

The charged operation is $U^\dagger$: it contains $G$ coherent gates per copy and generally couples different input sites. The local theorem grants classical access to the same circuit description, but does not permit these coherent gates for free.

This comparison places the inverse **before detector reporting noise**. It does not establish that inverse preparation corrects an already acquired depolarized state. For an entangling $U$, in general

$$
U^\dagger\mathcal D_q^{\otimes n}
\bigl(U|0^n\rangle\langle0^n|U^\dagger\bigr)U
\ne
\mathcal D_q^{\otimes n}(|0^n\rangle\langle0^n|).
\tag{25}
$$

The channel is covariant under separate one-qubit rotations, not arbitrary entangling unitaries. The global span test in Section 3 is the established comparison after the acquisition layer; its efficient implementation remains a separate question.

## 7. Resource summary

| Architecture | Binary copy cost for the stated generic targets | Resource determining the comparison |
|---|---:|---|
| One noisy destructive local report per site | $b^{-n+o(n)}$ | One detector use per input qubit; arbitrary classical strategy optimization |
| Arbitrary copywise separable POVM after one local acquisition layer | $b^{-n+o(n)}$ | All one-copy local processing is allowed; no coherent coupling of source copies |
| Global span measurement after acquisition, $q<q_*$ | One copy with vanishing error | A target-dependent global projector, with no efficient implementation claim |
| Clean inverse preparation before detector noise | $O_q(1)$ | $G$ coherent inverse gates and one detector report per copy |
| QND or local ancilla repetition before independent report errors | The ideal protocol's copy cost at fixed accuracy | $O_q(\log n)$ reports per qubit, plus the specified QND or ancilla resources |

The exponential local law quantifies the cost of the restricted acquisition architecture. It does not say that the target information has vanished globally, or that improving the architecture cannot recover it.

## References used on this page

- C. Lupo, M. M. Wilde, and S. Lloyd, *Quantum Data Hiding in the Presence of Noise*, IEEE Transactions on Information Theory **62**, 3745–3756 (2016). [Primary preprint](https://arxiv.org/pdf/1507.06038).
- G. Liu, C. Qin, Z. Xu, X. Ma, and Z.-W. Liu, *Can scrambling protect quantum state distinguishability under noise?*, arXiv:2606.02122 (2026). [Primary record](https://arxiv.org/abs/2606.02122), [institutional abstract](https://quics.umd.edu/publications/can-scrambling-protect-quantum-state-distinguishability-under-noise), and [public full manuscript](https://www.researchgate.net/publication/405682986_Can_scrambling_protect_quantum_state_distinguishability_under_noise).
- F. G. S. L. Brandão, A. W. Harrow, and M. Horodecki, *Local random quantum circuits are approximate polynomial-designs*, Communications in Mathematical Physics **346**, 397–434 (2016). [Corrected primary preprint](https://arxiv.org/pdf/1208.0692), Section III, Application I, for inverse-preparation discrimination.
- Z. Du, J. Liu, E. X. Huber, Z.-W. Liu, and X. Ma, *Certifying localizable quantum properties with constant sample complexity*, Physical Review X **16**, 041027 (2026). [Primary version 3](https://arxiv.org/html/2509.17580v3), Section VII.
- W. Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*, Journal of the American Statistical Association **58**, 13–30 (1963). [Primary article](https://doi.org/10.1080/01621459.1963.10500830). The bounded-variable estimates in (17), (23), and (24).
