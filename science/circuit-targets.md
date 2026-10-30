# Polynomial circuit targets

The exponential binary sample law extends to an explicitly quantified family of approximate state designs. Consequently, the hard targets need not require an exponentially long preparation circuit. A polynomial circuit description also supplies a useful comparison: if its coherent inverse is permitted before the detectors, the same target-versus-maximally-mixed promise has constant copy complexity.

The two resource statements are different. The local converse grants unlimited classical computation of the supplied target description. The coherent comparison pays for entangling gates. Neither statement assumes free amplitude loading.

## 1. Moment convention and result

Throughout, $`d=2^n`$, $`\tau=I/d`$, and a pure state is denoted by its projector $`\psi=|\psi\rangle\langle\psi|`$. Fix $`0\lt q\lt 1/2`$, and put

```math
s=1-2q,\qquad a=1-q,\qquad
b=a^2+q^2=\frac{1+s^2}{2}.
```

For a distribution $`\nu`$ of pure states, define its $`t`$-th moment operator by

```math
M_t(\nu)=\mathbb E_{\psi\sim\nu}\psi^{\otimes t}.
```

We use the following **additive trace-norm convention**:

```math
\begin{gathered}
\|M_t(\nu)-M_t(\mathrm{Haar})\|_1\le\epsilon,
\qquad
M_t(\mathrm{Haar})
=\frac{\Pi_{\mathrm{sym}}^{(t)}}{\binom{d+t-1}{t}}.
\end{gathered}
\tag{1}
```

There is no factor $`1/2`$ in (1). Partial trace shows that the same error bound holds at every order $`j\le t`$. In particular, for any operator $`A`$ on $`j`$ copies,

```math
\begin{gathered}
\left|
\mathbb E_\nu\mathrm{tr}(A\psi^{\otimes j})
-\mathbb E_{\mathrm{Haar}}\mathrm{tr}(A\psi^{\otimes j})
\right|
\le \epsilon\|A\|_\infty.
\end{gathered}
\tag{2}
```

**Theorem 1 — binary sample law for approximate designs.** There are universal sufficiently large constants $`\kappa,K`$ such that the following holds. Let

```math
\begin{gathered}
t_n=2\lceil\kappa n^2\rceil,\qquad
\epsilon_n\le e^{-K n^3},
\end{gathered}
\tag{3}
```

and suppose $`\nu_n`$ satisfies (1) with these parameters. For every fixed $`q\in(0,1/2)`$ and all sufficiently large $`n`$, with probability at least $`1-C_qe^{-c_qn}`$ over the target $`\psi\sim\nu_n`$, the optimal deterministic copy budget for distinguishing $`\psi`$ from $`\tau`$, with each error at most $`1/3`$, obeys

```math
\begin{gathered}
\frac{c_q}{n^2}\,b^{-n}
\ \le\ N^*(\psi,q)\ \le\ C_q b^{-n}.
\end{gathered}
\tag{4}
```

The measurement architecture, including arbitrary target-dependent axes, classical feedforward and interleaving of independent copies, is the one in [Model and results](model-and-results.md) and [Binary sample law](binary-sample-law.md). Thus

```math
\frac{\log N^*(\psi,q)}{n}\longrightarrow-\log b
```

in probability under $`\nu_n`$. The upper bound is a known-distribution likelihood-ratio test; its classical computation need not be efficient.

The constants in [Uniform concentration](uniform-concentration.md) permit the concrete sufficient choice

```math
\begin{gathered}
\kappa=32,\qquad K=160.
\end{gathered}
\tag{5}
```

These constants are deliberately conservative. They specify one sufficient design accuracy, rather than a necessary design order or an optimized circuit depth.

## 2. Transferring the uniform product-effect event

For unit Bloch balls $`|u_j|\le1`$, consider

```math
\begin{gathered}
E=\bigotimes_{j=1}^n\frac{I+s\,u_j\cdot\sigma}{2},
\qquad
r_E(\psi)=d\,\mathrm{tr}(\psi E)-1.
\end{gathered}
\tag{6}
```

Every factor has trace one. The spectral and purity bounds are

```math
\begin{gathered}
\mathrm{tr}(E^2)\le b^n,\qquad
q^n I\le E\le a^n I.
\end{gathered}
\tag{7}
```

For $`A=E-I/d`$ and $`B=dE-I=dA`$, these imply

```math
\begin{gathered}
\mathrm{tr}(A^2)\le b^n-\frac1d,\qquad
\|A\|_\infty\le a^n-\frac1d,\qquad
\|B\|_\infty\le d a^n.
\end{gathered}
\tag{8}
```

The second inequality follows because
$`a^n+q^n\ge 2/d`$, so the possible negative eigenvalue deviation is no larger than the positive bound.

The Haar moment estimate proved in [Uniform concentration](uniform-concentration.md) is

```math
\begin{gathered}
\|r_E\|_{L^{2m}(\mathrm{Haar})}
\le
2\sqrt{m\left(b^n-\frac1d\right)}
+3m\left(a^n-\frac1d\right)
\le 3\left(\sqrt m\,b^{n/2}+m a^n\right).
\end{gathered}
\tag{9}
```

Its mechanism is elementary: write a complex Gaussian vector as $`g=\sqrt G\,|\psi\rangle`$, with $`G=\|g\|^2`$ independent of the Haar direction. The centered quadratic form $`g^\dagger A g`$ is a weighted sum of independent centered exponential variables. A Bernstein moment bound applies, and

```math
\begin{gathered}
\mathbb E_{\mathrm{Haar}}r_E^{2m}
=\frac{d^{2m}}{d(d+1)\cdots(d+2m-1)}
\,\mathbb E(g^\dagger A g)^{2m}.
\end{gathered}
\tag{10}
```

The prefactor is at most one. This avoids a separate random-normalization error.

Because $`r_E^{2m}=\mathrm{tr}(B^{\otimes 2m}\psi^{\otimes 2m})`$, the approximate-design condition gives

```math
\begin{gathered}
\mathbb E_\nu r_E^{2m}
\le
\mathbb E_{\mathrm{Haar}}r_E^{2m}
+\epsilon(d a^n)^{2m},
\qquad 2m\le t.
\end{gathered}
\tag{11}
```

This is the entire additional approximation cost. In particular, one cannot transfer an exponentially small relative-fluctuation claim using a dimension-independent design error without checking (11).

### A finite parameter bound

Use a product Bloch-ball net at the same mesh as in the Haar proof:

```math
h_n=\frac{1}{4n\,4^n},
```

The volume argument used for the Haar sphere net also bounds this ball net by $`\exp(14n^2)`$ points. Tensor telescoping gives

```math
\begin{gathered}
|r_E(\psi)-r_{E'}(\psi)|
\le \frac{dn h_n}{2}
=\frac{1}{8d}
\end{gathered}
\tag{12}
```

for a nearest net point $`E'`$. Set

```math
\begin{gathered}
m=32n^2,\qquad
\delta_n=1024\left[n b^{n/2}+n^2 a^n\right].
\end{gathered}
\tag{13}
```

The moment bound in (9), divided by $`\delta_n/2`$, is at most $`3/16`$. Markov's inequality, (11), and a union bound therefore give

```math
\begin{aligned}
\Pr_\nu\!\left\{\sup_E|r_E(\psi)|\gt \delta_n\right\}
&\le
e^{14n^2}
\left[
\left(\frac{3}{16}\right)^{64n^2}
+\epsilon
\left(\frac{2da^n}{\delta_n}\right)^{64n^2}
\right].
\end{aligned}
\tag{14}
```

The extension error in (12) is smaller than $`\delta_n/2`$. Also,
$`2da^n/\delta_n\le d`$. Hence the first term in (14) is at most $`e^{-80n^2}`$, while $`\epsilon\le e^{-160n^3}`$ makes the second term at most

```math
\begin{gathered}
\exp\!\left[
14n^2-(160-64\log 2)n^3
\right]\le e^{-80n^2}.
\end{gathered}
\tag{15}
```

Here and below unmarked logarithms are natural. We have proved

```math
\begin{gathered}
\Pr_\nu\!\left\{
\sup_E|d\,\mathrm{tr}(\psi E)-1|\gt \delta_n
\right\}\le 2e^{-80n^2}.
\end{gathered}
\tag{16}
```

For fixed $`q\gt 0`$, $`a/\sqrt b\lt 1`$, so
$`\delta_n=O_q(n b^{n/2})`$. The uniform event in (16) is therefore exactly the input needed by the adaptive transcript argument. That argument gives

```math
D(P_\psi\|P_\tau)\le N\delta_n^2
```

for the complete classical transcript, including deterministic stopping and permitted interleaving. If both testing errors are at most $`1/3`$, Pinsker's inequality requires
$`D(P_\psi\|P_\tau)\ge2/9`$. This proves the lower bound in (4).

The use of high moments to transfer concentration from Haar measure to designs is established methodology; Low's [large-deviation theorem and product-state net application](https://arxiv.org/pdf/0903.5236), Theorem 1.2 and Section 6, are useful precedents. The specific transfer above keeps the noise-dependent relative-fluctuation scale and the additive trace-norm error explicit.

## 3. Transferring the matching fixed-basis test

Measure each qubit in the computational basis and apply the BSC readout. Let $`P_\psi`$ denote the resulting distribution and $`U`$ the uniform distribution on $`n`$ bits. Its chi-square divergence is

```math
\begin{gathered}
Q(\psi)=\chi^2(P_\psi\|U)
=\sum_{\varnothing\ne S\subseteq[n]}
s^{2|S|}\,[\mathrm{tr}(\psi Z_S)]^2.
\end{gathered}
\tag{17}
```

Define

```math
\begin{gathered}
W=(1+s^2)^n-1,\qquad
V=(1+s^4)^n-1,\qquad
\mu=\frac{W}{d+1}.
\end{gathered}
\tag{18}
```

The exact Haar calculation in [Binary sample law](binary-sample-law.md) gives

```math
\begin{gathered}
\mathbb E_{\mathrm{Haar}}Q=\mu,\qquad
v_n:=\frac{\mathrm{Var}_{\mathrm{Haar}}Q}{\mu^2}
=
\frac{2d[(d+1)V+W^2]}{(d+2)(d+3)W^2}.
\end{gathered}
\tag{19}
```

To transfer both moments, write

```math
C=\sum_{\varnothing\ne S\subseteq[n]}
s^{2|S|} Z_S\otimes Z_S.
```

Then $`Q=\mathrm{tr}(C\psi^{\otimes2})`$,
$`Q^2=\mathrm{tr}[(C\otimes C)\psi^{\otimes4}]`$, and
$`\|C\|_\infty\le W`$. Equation (2) therefore yields

```math
\begin{gathered}
\left|\mathbb E_\nu Q-\mu\right|\le\epsilon W,
\qquad
\left|\mathbb E_\nu Q^2-\mathbb E_{\mathrm{Haar}}Q^2\right|
\le\epsilon W^2.
\end{gathered}
\tag{20}
```

Centering at the Haar mean, rather than at an unknown design mean, gives the useful explicit bound

```math
\begin{gathered}
\Pr_\nu\{|Q-\mu|\gt \mu/2\}
\le
4v_n+4\epsilon(d+1)(d+3).
\end{gathered}
\tag{21}
```

For fixed $`0\lt s\lt 1`$,

```math
\begin{gathered}
\frac{1+s^4}{(1+s^2)^2}\lt 1,\qquad
v_n=O_q\!\left[
\left(\frac{1+s^4}{(1+s^2)^2}\right)^n+2^{-n}
\right].
\end{gathered}
\tag{22}
```

Moreover $`\mu=(1+o(1))b^n`$. The approximation term in (21) is negligible at the accuracy in (3).

On the intersection of (16) and the good event in (21), all likelihood ratios $`L_z=P_\psi(z)/U(z)`$ lie in $`[1-\delta_n,1+\delta_n]`$, and $`Q\ge\mu/2`$. For sufficiently large $`n`$, $`\delta_n\le1/2`$. With the convention

```math
H^2(P_\psi,U)=\sum_z
\left(\sqrt{P_\psi(z)}-\sqrt{U(z)}\right)^2,
```

we have

```math
\begin{gathered}
H^2(P_\psi,U)
=\mathbb E_U
\frac{(L_z-1)^2}{(\sqrt{L_z}+1)^2}
\ge
\frac{Q}{(1+\sqrt{3/2})^2}
=\Omega_q(b^n).
\end{gathered}
\tag{23}
```

The Bhattacharyya affinity of $`N`$ independent records is

```math
\left(1-\frac{H^2(P_\psi,U)}2\right)^N
\le e^{-N H^2(P_\psi,U)/2}.
```

The sum of the two errors of the likelihood-ratio test is at most this affinity. Thus $`N=O_q(b^{-n})`$ achieves both errors at most $`1/3`$. Combining (16), (21), and (22) proves the probability statement in Theorem 1.

## 4. A polynomial preparation construction and its precision

The moment convention in (1) must be related to the convention of the circuit construction. Let

```math
\mathcal T_{\mu,t}(X)
=\mathbb E_{U\sim\mu}
U^{\otimes t}X(U^\dagger)^{\otimes t}.
```

Brandão, Harrow, and Horodecki (BHH) use a stronger relative completely-positive-order condition,

```math
\begin{gathered}
(1-\eta)\mathcal T_{\mathrm{Haar},t}
\preceq_{\mathrm{CP}}\mathcal T_{\mu,t}
\preceq_{\mathrm{CP}}
(1+\eta)\mathcal T_{\mathrm{Haar},t}.
\end{gathered}
\tag{24}
```

Their Lemma 3 gives
$`\|\mathcal T_{\mu,t}-\mathcal T_{\mathrm{Haar},t}\|_\diamond\le2\eta`$.
Applying this channel to $`(|0^n\rangle\langle0^n|)^{\otimes t}`$ proves (1) with $`\epsilon=2\eta`$. These are the definitions and constants of the [corrected primary version](https://arxiv.org/pdf/1208.0692), Definition 2, Lemma 3, and Corollaries 6–7.

For qubits, their sequential nearest-neighbor Haar-gate construction has the sufficient gate count

```math
\begin{aligned}
G=
\Big\lceil
170000\,n\,\lceil\log_2(4t)\rceil^2
t^{\,5+3.1/\log 2}
\bigl[2nt\log2+\log(1/\eta)\bigr]
\Big\rceil,
\end{aligned}
\tag{25}
```

where the displayed integer can be used as the construction length. Equivalently, a circuit of this length suffices; no optimality of the bound is asserted.

There is also a finite-alphabet version. Fix a universal finite set $`\mathcal G\subset SU(4)`$ with algebraic matrix entries and containing the inverse of each of its gates. BHH's Corollary 7 gives

```math
\begin{gathered}
G=
O_{\mathcal G}\!\left(
n\,\lceil\log_2(4t)\rceil^2
t^{\,5+3.1/\log2}
[nt+\log(1/\eta)]
\right)
\end{gathered}
\tag{26}
```

nearest-neighbor gates. The implicit constant depends on the fixed gate alphabet; BHH does not give a numerical value for that gate-set-dependent constant. A circuit is sampled by choosing a neighboring pair and a gate from $`\mathcal G`$ at each step.

Choose $`t=64n^2`$ and $`\eta=\tfrac14e^{-160n^3}`$. Since $`5+3.1/\log2\lt 9.5`$, (26) is, conservatively,

```math
\begin{gathered}
G=O_{\mathcal G}(n^{23}\log^2 n).
\end{gathered}
\tag{27}
```

The construction therefore uses a polynomial number of gates and bits in its classical gate-list description. Exact uniform selection of locations and gate labels uses a polynomial expected number of fair random bits, for example by rejection sampling. This is an asymptotic existence construction with a large polynomial; it is not a shallow-circuit claim. The finite alphabet permits exact specification of the ideal logical circuit without listing exponentially many target amplitudes.

### If continuous gates are rounded

For completeness, the accuracy cost can also be stated directly. Suppose a $`G`$-gate circuit $`U`$ is replaced by $`\widetilde U`$, with operator-norm error at most $`\zeta`$ at each gate, after a consistent choice of irrelevant global phases. Telescoping gives

```math
\|U-\widetilde U\|_\infty\le G\zeta,
\qquad
\|\psi-\widetilde\psi\|_1\le2G\zeta.
```

Telescoping tensor powers and then averaging the coupled circuit ensembles yield

```math
\begin{gathered}
\|M_t(\nu)-M_t(\widetilde\nu)\|_1
\le 2tG\zeta.
\end{gathered}
\tag{28}
```

If the ideal ensemble has moment error at most $`\epsilon/2`$, choosing

```math
\begin{gathered}
\zeta\le\frac{\epsilon}{4tG}
\end{gathered}
\tag{29}
```

preserves the total error $`\epsilon`$. At $`\epsilon=e^{-160n^3}`$, this requires $`O(n^3+\log(tG))`$ bits of precision per constant-size matrix entry. The required numerical description is polynomial in length. Equation (29) is a sufficient synthesis or representation error budget, not a claim of tolerance to physical gate noise. The finite-alphabet construction in (26) is the cleaner ideal-gate statement.

## 5. Matched access: a supplied coherent inverse

Suppose the same target is supplied by a known preparation circuit
$`U`$, so $`|\psi\rangle=U|0^n\rangle`$. In the **detector-noise model**, allow the verifier to apply the ideal coherent circuit $`U^\dagger`$ before any destructive readout. Under the two hypotheses,

```math
U^\dagger\psi U=|0^n\rangle\langle0^n|,
\qquad
U^\dagger\tau U=\tau.
```

Measure just the first qubit in the computational basis through its BSC detector. The probability of reporting zero is

```math
\begin{gathered}
\Pr(0\mid\psi)=1-q,\qquad
\Pr(0\mid\tau)=\frac12.
\end{gathered}
\tag{30}
```

The gap is $`s/2`$, independent of $`n`$. Thresholding the empirical zero frequency halfway between these probabilities gives, by Hoeffding's inequality, each error at most

```math
\begin{gathered}
\exp(-Ns^2/8).
\end{gathered}
\tag{31}
```

Thus

```math
\begin{gathered}
N\ge\left\lceil\frac{8}{s^2}\log\frac1\alpha\right\rceil
\end{gathered}
\tag{32}
```

suffices for each error at most $`\alpha`$. For fixed $`q\lt 1/2`$ and constant $`\alpha`$, this is constant copy complexity with $`G`$ coherent inverse gates and one detector report per copy. In an inverse-closed gate alphabet, reversing the gate list implements $`U^\dagger`$ with the same gate count.

Only constant accuracy of the complete inverse is needed for this binary advantage. For example, $`\|V-U^\dagger\|_\infty\le s/8`$ changes the target's reported-zero probability by at most $`s/8`$, retaining a constant gap. A sufficient independent gate-error budget is then $`O(s/G)`$ in operator norm per inverse gate. This accuracy requirement should not be confused with the much stronger sufficient ensemble-moment accuracy in (29).

Both strategies receive the same target circuit and the same independent-copy source. If source preparation is counted, both also pay its $`G`$ gates for every copy; the coherent strategy additionally pays the inverse circuit. The converse does not restrict classical computations on that gate list. The separation is therefore between permitted coherent readout architectures, not between different amounts of target advice.

Inverse-preparation discrimination is already described in BHH's Section III, Application I. Here it supplies a matched binary comparison with the BSC detector cost made explicit.

Applying $`U^\dagger`$ **after** an irreversible local depolarization layer is a different operation and need not produce the probabilities in (30). The separate global test for that acquisition model is proved in [Acquisition and control](acquisition-and-control.md).

## 6. Scope of the transfer

The proof transfers the binary testing law because it uses finitely many polynomial moments of the target and a controlled product-effect net. It does **not** by itself transfer Du et al.'s constant spectral gap for their full-fidelity verification operator. That property needs its own argument for the selected circuit ensemble.

Accordingly, the Haar full-fidelity noise-budget result in [Fidelity certification](fidelity-certification.md) and the circuit-ensemble binary theorem above have distinct stated scopes. Neither the fixed-basis likelihood test nor the coherent one-bit test is asserted here to certify fidelity against every alternative state.

## References used on this page

- R. A. Low, *Large Deviation Bounds for $`k`$-designs*, Proceedings of the Royal Society A **465**, 3289–3308 (2009). [Primary preprint](https://arxiv.org/pdf/0903.5236). High-moment transfer and product-state nets.
- F. G. S. L. Brandão, A. W. Harrow, and M. Horodecki, *Local random quantum circuits are approximate polynomial-designs*, Communications in Mathematical Physics **346**, 397–434 (2016). [Corrected primary preprint, version 4](https://arxiv.org/pdf/1208.0692). Design conventions, polynomial random circuits, finite gate sets, and inverse-preparation discrimination.
- Z. Du, J. Liu, E. X. Huber, Z.-W. Liu, and X. Ma, *Certifying localizable quantum properties with constant sample complexity*, Physical Review X **16**, 041027 (2026). [Primary version 3](https://arxiv.org/html/2509.17580v3). The distinct Haar full-fidelity gap result.
- W. Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*, Journal of the American Statistical Association **58**, 13–30 (1963). [Primary article](https://doi.org/10.1080/01621459.1963.10500830). The bounded-outcome tail estimate in (31).

The full attribution of the inherited noisy fixed-basis moment scale appears in [Related work](../references/RELATED_WORK.md).
