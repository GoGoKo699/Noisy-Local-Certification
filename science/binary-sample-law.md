# Optimal copy complexity for a known target versus the maximally mixed state

We consider the binary promise that every supplied copy is either a known pure state $\psi$ or the maximally mixed state $\tau=I/2^n$. Each input qubit supplies at most one destructive projective measurement report, independently corrupted by a known binary symmetric channel. Complete knowledge of the target, unlimited classical computation, and arbitrary classical feedback are allowed.

The main result identifies the optimal exponential copy rate. A fixed computational basis attains that rate. The converse applies to all allowed protocols, including protocols that interleave measurements of different copies.

All logarithms are natural. We use the notation

$$
d=2^n,\qquad s=1-2q,\qquad a=1-q,\qquad
b=\frac{1+s^2}{2}=(1-q)^2+q^2.
$$

Let $C_{\mathrm{unif}}=1024$ and

$$
\delta_n(q)=C_{\mathrm{unif}}
\left[n b^{n/2}+n^2a^n\right]. \tag{1}
$$

The event $\mathcal U_{n,q}$ is the simultaneous likelihood event of [Theorem 1 in the concentration chapter](uniform-concentration.md). It has Haar probability at least $1-e^{-80n^2}$ and controls normalized effects of both complete and partial local records.

## 1. Protocol and error conventions

Fix the target $\psi$ and the calibrated error probability $q$. A protocol with deterministic copy budget $N$ has access to at most $N$ independent $n$-qubit input copies. At each step it may select any unread site of any available copy, choose a projective measurement axis, observe its corrupted report, or halt. These choices may depend on the full target description, all earlier reports, and private classical randomness. Unread qubits may wait while another copy is measured.

The permitted measurement on a selected site has ideal projectors

$$
P_z(v)=\frac{I+z\,v\cdot\sigma}{2},
\qquad z\in\{+1,-1\},\quad v\in S^2.
$$

Only the reported sign $y$ is available to the protocol. It equals $z$ with probability $1-q$ and $-z$ with probability $q$, independently at every measured site. The measured qubit is discarded. There are no joint quantum operations between input sites or between copies, no additional reports from a measured site, and no access to the unreported ideal sign. Single-qubit basis changes are included in the choice of $v$.

The final output is a classical decision between the two hypotheses

$$
H_1:\psi^{\otimes N},
\qquad
H_0:\tau^{\otimes N}.
$$

Copies not requested before the protocol halts can be regarded as supplied and left unread. Their measurement effect is the identity. Thus adaptive stopping and adaptive allocation of copies are included under the deterministic cap $N$.

For $0<\varepsilon<1/2$, let $N_{\mathrm{opt}}(\psi,q,\varepsilon)$ denote the least such budget for which **both** conditional error probabilities are at most $\varepsilon$. The value is infinity if no finite budget suffices. Define

$$
k_\varepsilon=(1-2\varepsilon)
\log\frac{1-\varepsilon}{\varepsilon}>0. \tag{2}
$$

## 2. A transcript identity that covers arbitrary interleaving

The converse uses full transcript likelihoods. A partial measurement record on each copy is retained in the analysis, even when the actual protocol outputs only one final bit.

### Lemma 1. Product effects for a complete recorded transcript

Include all private classical randomness in an initial seed $R$ with its prescribed distribution. Conditional on the seed, the protocol is a deterministic binary decision tree of depth at most $nN$. For a terminal recorded transcript $t$, let $J_i(t)$ be the sites measured in input copy $i$. The effect contributed by that copy is

$$
H_i(t)=
\bigotimes_{j\in J_i(t)}
\frac{I+s\,y_{ij}(t)v_{ij}(t)\cdot\sigma}{2}
\;\otimes\!
\bigotimes_{j\notin J_i(t)} I. \tag{3}
$$

The axes, reported signs, and measured subsets in (3) are those specified by this complete branch. For any independent source states $\rho_1,\ldots,\rho_N$, the transcript probability density is

$$
p_{\rho_1,\ldots,\rho_N}(t)
=c(t)\prod_{i=1}^N\operatorname{tr}\!\left(\rho_iH_i(t)\right), \tag{4}
$$

where $c(t)$ is common to all source states. One may take the reference measure to be the seed distribution times counting measure on finite report strings, in which case $c(t)$ is just the indicator that the branch is allowed by the protocol.

#### Proof

For a specified reported sign $y$, summing over the inaccessible ideal sign gives the local effect

$$
\sum_{z=\pm1}\Pr(y\mid z)P_z(v)
=\frac{I+s\,y v\cdot\sigma}{2}. \tag{5}
$$

On a fixed reported branch, every later choice of axis and site is fixed. Since each site is measured at most once, the ideal projectors acting at different sites commute and have disjoint support. Summing over all inaccessible ideal signs factorizes the product of their independent reporting probabilities, giving (3). Unread sites contribute the identity.

The complete effect is $\bigotimes_iH_i(t)$ because the same reasoning applies across different input copies. Taking its expectation on the product source state gives (4). Feedback changes which product effect labels a branch; it does not change this factorization for that branch. Including the seed makes all randomized choices part of the same argument. $\square$

Normalize each factor by its trace:

$$
\overline H_i(t)=\frac{H_i(t)}{\operatorname{tr}H_i(t)},
\qquad
\operatorname{tr}H_i(t)=2^{n-|J_i(t)|}.
$$

This normalization puts $I/2$ on every unread site. Define

$$
\ell_i(t)=
\frac{\operatorname{tr}(\psi H_i(t))}
{\operatorname{tr}(\tau H_i(t))}
=d\,\operatorname{tr}(\psi\overline H_i(t)). \tag{6}
$$

On $\mathcal U_{n,q}$,

$$
|\ell_i(t)-1|\leq\delta_n(q) \tag{7}
$$

simultaneously for every copy, every branch, and every target-informed protocol.

### Lemma 2. Hybrid relative-entropy identity

Let $P$ be the refined transcript law when all source copies are $\psi$, and let $Q$ be its law when all source copies are $\tau$. Let $P^{(i)}$ be the law of the **same protocol**, with only source copy $i$ replaced by $\tau$ and all other copies still equal to $\psi$. The protocol is not told about this replacement and its target description remains $\psi$. Then

$$
\frac{dP}{dQ}(t)=\prod_{i=1}^N\ell_i(t),
\qquad
\frac{dP}{dP^{(i)}}(t)=\ell_i(t), \tag{8}
$$

on the respective supports. Consequently, on $\mathcal U_{n,q}$,

$$
\boxed{\quad
D(P\|Q)
=\sum_{i=1}^N D(P\|P^{(i)})
\leq N\,\delta_n(q)^2.
\quad} \tag{9}
$$

Here $D$ is classical relative entropy in natural logarithms.

#### Proof

Equation (4) gives both likelihood identities in (8). Every allowed local record has strictly positive probability under a maximally mixed input. Thus $P\ll Q$ and $P\ll P^{(i)}$, including when $q=0$ and some target probabilities vanish.

On the support of $P$, all factors in (8) are positive. Taking logarithms and then expectation under $P$ gives the identity in (9). Each $P^{(i)}$ is a normalized transcript distribution of a physical run of the fixed protocol; this fact is needed for the next step.

For any probability measures $P\ll H$, with likelihood ratio $L=dP/dH$, the inequality $\log x\leq x-1$ gives

$$
\begin{aligned}
D(P\|H)
&=\mathbb E_H[L\log L]\\
&\leq\mathbb E_H[L(L-1)]\\
&=\mathbb E_H[(L-1)^2],
\end{aligned} \tag{10}
$$

where $\mathbb E_H L=1$ was used. Applying (10) with $H=P^{(i)}$, and then using (7), yields $D(P\|P^{(i)})\leq\delta_n^2$. This also proves that all terms in (9) are finite, so the expectation of their finite sum is justified. The convention $0\log0=0$ handles vanishing likelihoods.

No condition $\delta_n<1$ is required for this converse. Actual likelihoods are nonnegative, and (7) alone bounds their squared deviations. $\square$

This identity removes any penalty for cross-copy interleaving. A stepwise bound that charged every recorded bit separately would be weaker. Halting is already covered by the identity effects on unread sites and unused copies. Forgetting the private seed, coarse-graining the reports, or keeping only the final decision cannot increase relative entropy.

### Theorem 3. Finite-dimensional converse

On $\mathcal U_{n,q}$, every allowed protocol whose two conditional errors are at most $\varepsilon$ satisfies

$$
\boxed{\quad
N\geq\frac{k_\varepsilon}{\delta_n(q)^2}.
\quad} \tag{11}
$$

This holds for arbitrary classical interleaving and adaptive stopping under the deterministic copy cap.

#### Proof

Let $A$ be the event that the protocol outputs the target hypothesis. Its error conditions imply

$$
P(A)\geq1-\varepsilon,\qquad Q(A)\leq\varepsilon.
$$

The log-sum inequality, applied to $A$ and its complement, gives

$$
D(P\|Q)\geq
d_{\mathrm{Ber}}\!\left(P(A)\,\|\,Q(A)\right).
$$

For $p\geq1-\varepsilon>\varepsilon\geq r$, the binary relative entropy $d_{\mathrm{Ber}}(p\|r)$ increases with $p$ and decreases with $r$. Its minimum on this domain is therefore

$$
d_{\mathrm{Ber}}(1-\varepsilon\|\varepsilon)
=(1-2\varepsilon)\log\frac{1-\varepsilon}{\varepsilon}
=k_\varepsilon.
$$

Combine this inequality with (9). $\square$

For a simpler constant, set $x=1-2\varepsilon$ and use
$\log((1+x)/(1-x))\geq2x$. Then

$$
k_\varepsilon\geq2(1-2\varepsilon)^2. \tag{12}
$$

Since $a^2\leq b$ and $n+n^2\leq2n^2$, (11) also gives the uniform bound

$$
\boxed{\quad
N\geq
\frac{k_\varepsilon}{4C_{\mathrm{unif}}^2n^4b^n}
\geq
\frac{(1-2\varepsilon)^2}
{2C_{\mathrm{unif}}^2n^4b^n}.
\quad} \tag{13}
$$

In particular, for any prescribed sequence $q=q_n\in[0,1/2]$,

$$
N\geq
\frac{k_\varepsilon}{4C_{\mathrm{unif}}^2n^4}
\exp\!\left[2nq_n(1-q_n)\right] \tag{14}
$$

on an event of Haar probability at least $1-e^{-80n^2}$. If $nq_n/\log n\to\infty$, this lower bound is superpolynomial for every fixed $\varepsilon<1/2$.

## 3. Fixed-basis statistics and exact Haar moments

To prove achievability for the binary promise, measure every copy in the computational basis. Let

$$
p_0(z)=|\langle z|\psi\rangle|^2,\qquad
z\in\{0,1\}^n,
$$

and let $p=p_{\psi,q}$ be its distribution after independent bit flips:

$$
p(x)=\sum_{z\in\{0,1\}^n}
q^{|x\oplus z|}(1-q)^{n-|x\oplus z|}p_0(z). \tag{15}
$$

The alternative $\tau$ gives the uniform distribution $u(x)=1/d$.

For $S\subseteq\{1,\ldots,n\}$, let $Z_S$ act as Pauli $Z$ on $S$ and identity elsewhere, and put

$$
m_S=\langle\psi|Z_S|\psi\rangle.
$$

The Walsh character $\chi_S(x)=(-1)^{\sum_{j\in S}x_j}$ has expectation $s^{|S|}m_S$ under $p$. Walsh inversion and Parseval's identity give

$$
p(x)=\frac1d\left[
1+\sum_{S\ne\varnothing}s^{|S|}m_S\chi_S(x)
\right]
$$

and

$$
\boxed{\quad
Q_\psi:=\chi^2(p\|u)
=d\sum_x\left(p(x)-\frac1d\right)^2
=\sum_{S\ne\varnothing}s^{2|S|}m_S^2.
\quad} \tag{16}
$$

### Lemma 4. Exact first and second moments of $Q_\psi$

For $s>0$, define

$$
W=(1+s^2)^n-1,\qquad V=(1+s^4)^n-1.
$$

Then

$$
\mu_n:=\mathbb E Q_\psi=\frac{W}{d+1}, \tag{17}
$$

$$
\mathbb E Q_\psi^2
=\frac{(d+6)W^2+2dV}
{(d+1)(d+2)(d+3)}, \tag{18}
$$

and

$$
\boxed{\quad
R_n:=\frac{\operatorname{Var}(Q_\psi)}{\mu_n^2}
=\frac{2d\left[(d+1)V+W^2\right]}
{(d+2)(d+3)W^2}.
\quad} \tag{19}
$$

#### Proof

The Haar moment identity is

$$
\mathbb E\,\psi^{\otimes r}
=\frac{1}{(d)_r}\sum_{\pi\in S_r}U_\pi, \tag{20}
$$

where $U_\pi$ permutes the tensor factors. One direct derivation uses the Gaussian representation from the concentration chapter: the complex Gaussian moment identity gives
$\mathbb E(gg^*)^{\otimes r}=\sum_{\pi\in S_r}U_\pi$, while radial independence gives
$\mathbb E(gg^*)^{\otimes r}=(d)_r\mathbb E\psi^{\otimes r}$. Equivalently, (20) is the normalized projector onto the symmetric subspace.

For a nonempty $S$, $Z_S$ is traceless and $Z_S^2=I$. The $r=2$ instance of (20) therefore gives

$$
\mathbb E m_S^2=\frac{1}{d+1}. \tag{21}
$$

For distinct nonempty $S,T$, apply the $r=4$ identity to
$(Z_S,Z_S,Z_T,Z_T)$. A permutation with a fixed point contributes zero. Of the three permutations consisting of two transpositions, only the pairing of the two $Z_S$ factors and the two $Z_T$ factors contributes, giving $d^2$. The other two pairings contain $\operatorname{tr}(Z_SZ_T)=0$. Each of the six four-cycles contributes $d$, because the $Z$ strings commute and their total product is $I$. Thus

$$
\mathbb E[m_S^2m_T^2]
=\frac{d^2+6d}{(d)_4}
=\frac{d+6}{(d+1)(d+2)(d+3)}
\qquad(S\ne T). \tag{22}
$$

When $S=T$, all three pairings contribute $d^2$, and the six four-cycles still contribute $d$ each. Hence

$$
\mathbb E m_S^4
=\frac{3d^2+6d}{(d)_4}
=\frac{3}{(d+1)(d+3)}. \tag{23}
$$

The weights $w_S=s^{2|S|}$ obey
$\sum_{S\ne\varnothing}w_S=W$ and
$\sum_{S\ne\varnothing}w_S^2=V$. Substituting (21) into (16) proves (17). Substituting (22)–(23) into its square gives

$$
\mathbb E Q_\psi^2
=\frac{(d+6)(W^2-V)+3(d+2)V}
{(d+1)(d+2)(d+3)},
$$

which is (18). Subtracting $\mu_n^2$ and dividing by it yields (19). $\square$

For a fixed $0<s<1$, put

$$
\kappa_s=\frac{1+s^4}{(1+s^2)^2}<1.
$$

When $(1+s^2)^n\geq2$, equation (19) implies

$$
R_n
\leq\frac2d+2\frac{V}{W^2}
\leq2\cdot2^{-n}+8\kappa_s^n. \tag{24}
$$

Indeed, $W\geq(1+s^2)^n/2$ and $V\leq(1+s^4)^n$. Chebyshev's inequality now gives the explicit lower-tail bound

$$
\Pr\{Q_\psi<\mu_n/2\}\leq4R_n. \tag{25}
$$

It also proves $Q_\psi/\mu_n\to1$ in probability. Since

$$
\frac{\mu_n}{b^n}
=\frac{d}{d+1}\left[1-(1+s^2)^{-n}\right]\longrightarrow1, \tag{26}
$$

the fixed-basis chi-square divergence is $(1+o(1))b^n$ with high Haar probability.

## 4. From chi-square divergence to a test with controlled errors

The uniform event supplies the regularity needed to turn (16) into a sample bound at its reciprocal scale.

### Lemma 5. Hellinger and likelihood-test bound

Suppose $p$ is a distribution on $d$ points, $u$ is uniform, and

$$
\max_x|d p(x)-1|\leq\delta\leq\frac12.
$$

Writing $Q=\chi^2(p\|u)$, a likelihood-ratio test using $N$ independent samples has both error probabilities at most $\varepsilon$ whenever

$$
N\geq\frac{10}{Q}\log\frac1\varepsilon. \tag{27}
$$

#### Proof

Set $t_x=dp(x)-1$. Use the convention

$$
H^2(p,u)=\sum_x(\sqrt{p(x)}-\sqrt{u(x)})^2
$$

for squared Hellinger distance. Then

$$
\begin{aligned}
H^2(p,u)
&=\frac1d\sum_x
\frac{t_x^2}{(\sqrt{1+t_x}+1)^2}\\
&\geq\frac{Q}{5},
\end{aligned} \tag{28}
$$

because $(\sqrt{3/2}+1)^2<5$. The affinity satisfies

$$
A(p,u):=\sum_x\sqrt{p(x)u(x)}
=1-\frac{H^2(p,u)}2
\leq e^{-Q/10}. \tag{29}
$$

For $N$ samples the affinity is $A(p,u)^N$. The likelihood test chooses $p$ when $p^{\otimes N}\geq u^{\otimes N}$, with any fixed convention on ties. On a region where it makes an error under $p$, the density $p^{\otimes N}$ is at most $\sqrt{p^{\otimes N}u^{\otimes N}}$. On a region where it makes an error under $u$, the same statement holds with $u^{\otimes N}$. Therefore each conditional error is at most $A(p,u)^N\leq e^{-NQ/10}$. This proves (27). $\square$

For the noisy computational basis in (15), each outcome effect is a member of the product class controlled by $\mathcal U_{n,q}$. Thus the pointwise hypothesis of Lemma 5 holds with $\delta=\delta_n(q)$ whenever $\delta_n(q)\leq1/2$.

### Proposition 6. Finite-dimensional achievability

Let $0<q<1/2$ and suppose $\delta_n(q)\leq1/2$. Except on a set of Haar measure at most $e^{-80n^2}+4R_n$,

$$
\boxed{\quad
N_{\mathrm{opt}}(\psi,q,\varepsilon)
\leq
\left\lceil
\frac{20}{\mu_n}\log\frac1\varepsilon
\right\rceil.
\quad} \tag{30}
$$

The protocol uses the same computational basis on every copy and a classical likelihood test.

#### Proof

Intersect $\mathcal U_{n,q}$ with the event $Q_\psi\geq\mu_n/2$ from (25), and apply Lemma 5. The union bound does not require these events to be independent. $\square$

The distribution $p_{\psi,q}$ is known from the supplied target and calibration. Computing it and evaluating the likelihood may take exponential classical time. Equation (30) is a copy-complexity statement under the stated allowance of unlimited classical processing.

## 5. The optimal fixed-noise exponential rate

### Theorem 7. Binary sample law

Fix $q\in(0,1/2)$ and $\varepsilon\in(0,1/2)$. For all sufficiently large $n$, with Haar probability at least

$$
1-e^{-80n^2}-8\cdot2^{-n}-32\kappa_s^n,
$$

the optimal deterministic copy budget satisfies

$$
\boxed{\quad
\frac{k_\varepsilon}
{4C_{\mathrm{unif}}^2 n^2}\,b^{-n}
\leq N_{\mathrm{opt}}(\psi,q,\varepsilon)
\leq
\left\lceil40\,b^{-n}\log\frac1\varepsilon\right\rceil.
\quad} \tag{31}
$$

In particular,

$$
\frac1n\log N_{\mathrm{opt}}(\psi,q,\varepsilon)
\longrightarrow
-\log b
=-\log\!\left(\frac{1+(1-2q)^2}{2}\right) \tag{32}
$$

in probability over Haar targets.

#### Proof

All of the following conditions hold for sufficiently large $n$ at fixed $q\in(0,1/2)$:

$$
\delta_n(q)\leq\frac12,\qquad
n\left(\frac a{\sqrt b}\right)^n\leq1,\qquad
(1+s^2)^n\geq4. \tag{33}
$$

The first two use $b<1$ and $a/\sqrt b<1$; the third uses $s>0$. The second condition implies $\delta_n\leq2C_{\mathrm{unif}}n b^{n/2}$, so Theorem 3 gives the lower bound in (31). For the upper bound, (26), $d/(d+1)\geq2/3$, and the third condition give $\mu_n\geq b^n/2$. Proposition 6 then gives the upper bound in (31).

The failure estimate follows from (24)–(25) and the probability of $\mathcal U_{n,q}$. Taking logarithms of (31) and dividing by $n$ proves (32). $\square$

The displayed exceptional probabilities are summable in $n$. Thus, if targets at different sizes are placed on a common probability space with the stated Haar marginal distributions, (32) also holds almost surely by the first Borel–Cantelli lemma; independence across sizes is unnecessary.

The finite-$n$ result is (11) together with (30), using the full expression (1). The simplification in (31) is asymptotic. In particular, a small fixed error probability can require a large $n$ before the term $n^2a^n$ is dominated by $n b^{n/2}$.

## 6. Endpoints and certification scope

At $q=1/2$, every reported local effect equals $I/2$. The complete transcript law is then independent of the input state, even with adaptive axes and interleaving. Consequently $N_{\mathrm{opt}}=\infty$ for every $\varepsilon<1/2$.

At $q=0$, Haar-typical binary testing is possible with a constant number of copies at fixed error. This can be seen directly in the computational basis. Write $p_0(x)=Y_x/\sum_zY_z$ with independent mean-one exponentials $Y_x$. The affinity with uniform is

$$
A(p_0,u)=
\frac{d^{-1}\sum_x\sqrt{Y_x}}
{\sqrt{d^{-1}\sum_xY_x}}
\longrightarrow
\mathbb E\sqrt{Y}
=\frac{\sqrt\pi}{2}<1 \tag{34}
$$

in probability, by the law of large numbers. The affinity argument in Lemma 5, before its use of (28), gives a constant-copy test for any fixed $\varepsilon>0$.

A fidelity-certification protocol that must accept the exact target and reject $I/d$ inherits every converse above. In particular, any fixed infidelity rejection threshold below $1-d^{-1}$ includes the maximally mixed state among the alternatives. The achievability proof in this chapter assumes the binary promise $\{\psi,I/d\}$: it tests against a single known alternative. The optimal fixed-noise exponential rate for certification against all low-fidelity alternatives is not determined by (31).

## References and attribution

The factor $b^n$ in the fixed-basis calculation is the same Hilbert–Schmidt scale that appears in [Maciejewski, Puchała and Oszmaniec, *Operational Quantum Average-Case Distances*, Example 2](https://quantum-journal.org/papers/q-2023-09-11-1106/pdf/). Their companion [*Exploring Quantum Average-Case Distances: proofs, properties, and examples*, Example 10, Eq. (132)](https://arxiv.org/html/2112.14284v6) gives the exact measurement-distance expression $\tfrac12\sqrt{b^n-d^{-1}}$ for independent symmetric readout errors. The first moment in (17) is consistent with that expression.

The Haar symmetric-subspace moment formula used in (20), and the high-moment method behind the companion concentration theorem, belong to the standard design framework; see [Low, *Large Deviation Bounds for k-designs*](https://arxiv.org/pdf/0903.5236). The calculations (21)–(25) spell out the particular fourth-moment consequence needed here. The converse additionally uses uniform target-dependent effect control and the normalized hybrid transcript distributions in (8)–(9).
