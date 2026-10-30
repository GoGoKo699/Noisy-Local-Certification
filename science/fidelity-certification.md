# Detector-noise threshold for fidelity certification

For a Haar-typical known $n$-qubit target, constant-gap fidelity certification with one destructive local measurement per qubit has polynomial copy complexity precisely when the independent detector error satisfies

$$
 n q_n=O(\log n).
$$

Here certification accepts the exact target and rejects every state whose fidelity is below a fixed threshold. The sufficient protocol also accepts a constant neighborhood of the target, with the precise neighborhood determined by a verification-operator spectral gap. This is a statement about the number of input copies; the classical computation can be exponential.

The proof combines the target-informed converse from the [uniform product-effect theorem](uniform-concentration.md) with an explicit inversion of a bounded, nonadaptive local-Pauli score. The ideal observable and its Haar-typical spectral gap are due to Du et al.; the detector-noise inversion and its statistical bound are derived below.

## 1. Task, promises, and detector model

Let $\psi=|\psi\rangle\langle\psi|$ be a known pure target. The source supplies independent copies of one fixed, otherwise arbitrary density operator $\rho$. Write

$$
 F_\psi(\rho)=\langle\psi|\rho|\psi\rangle.
$$

Fix a confidence error $0<\alpha<1/2$ and infidelity parameters

$$
 0\leq\varepsilon_{\mathrm g}<\varepsilon_{\mathrm b}<1.
$$

A certificate must satisfy both of the following guarantees:

- If $F_\psi(\rho)\geq 1-\varepsilon_{\mathrm g}$, it accepts with probability at least $1-\alpha$.
- If $F_\psi(\rho)\leq 1-\varepsilon_{\mathrm b}$, it rejects with probability at least $1-\alpha$, uniformly over all such mixed or pure states.

No decision is prescribed in the intervening region. The case $\varepsilon_{\mathrm g}=0$ is exact-target certification. It requires high-probability acceptance when the prepared state equals the target; it does not require acceptance with probability one.

Each physical input qubit receives at most one destructive rank-one projective measurement. A true outcome bit $x_i$ is reported as

$$
 y_i=x_i\oplus e_i,\qquad e_i\sim\operatorname{Bernoulli}(q),
 \qquad 0\leq q<\tfrac12,
$$

independently across sites and copies. The common error probability is known. Measurement axes and their classical labels are ideal and known. The converse permits target-dependent axes, arbitrary classical feedback and interleaving of different copies, and unrestricted classical computation, subject to a deterministic cap on the number of copies. It does not permit entangling processing of the input qubits, joint quantum processing between source copies, repeated nondemolition detection, or ancilla encoding before readout.

The sufficient protocol uses a smaller class: every Pauli basis is selected before any outcome from that copy is observed. Consequently, its detector acts on a fixed classical outcome distribution through a product binary symmetric channel. This nonadaptivity is essential to the particular inversion argument below.

## 2. The target-dependent verification observable

Designate one qubit as $A$ and let $B$ contain the other $n-1$ qubits. For a Pauli basis pattern $\theta_B\in\{X,Y,Z\}^{n-1}$ and an outcome string $z\in\{0,1\}^{n-1}$, let $|z_{\theta_B}\rangle$ be the corresponding product eigenstate. Define

$$
 |v_{\theta_B,z}\rangle
   =(I_A\otimes\langle z_{\theta_B}|)\,|\psi\rangle,
 \qquad
 w_{\theta_B,z}=\langle v_{\theta_B,z}|v_{\theta_B,z}\rangle,
$$

and

$$
 T_{\theta_B,z}=
 \begin{cases}
 |v_{\theta_B,z}\rangle\langle v_{\theta_B,z}|/w_{\theta_B,z},
       &w_{\theta_B,z}>0,\\
 0,&w_{\theta_B,z}=0.
 \end{cases}
$$

Use the observable

$$
 O_\psi
 =3^{-(n-1)}
   \sum_{\theta_B,z}
   T_{\theta_B,z}\otimes
   |z_{\theta_B}\rangle\langle z_{\theta_B}|.
 \tag{1}
$$

This is Du et al.'s conditional-fidelity observable, their Eq. (33). Their Theorem 5, with the retained subsystem chosen to be one qubit, states that its spectral gap is bounded below by a positive universal constant except on a Haar set of probability $\exp[-\Omega(n)]$. Their Appendix A, Eq. (A2), gives the local-shadow score used to measure it; Appendix F.1 proves the fidelity promises associated with its gap. These are ideal-measurement statements. [Du et al., v3](https://arxiv.org/html/2509.17580v3)

For each fixed $\theta_B$, the summands in (1) act on orthogonal blocks of $B$, and each nonzero $T_{\theta_B,z}$ is a rank-one projector. Hence

$$
 0\leq O_\psi\leq I,
 \qquad O_\psi|\psi\rangle=|\psi\rangle.
$$

Define the target-specific gap

$$
 \gamma_\psi
 =1-\lambda_{\max}\!\left(O_\psi\big|_{\psi^\perp}\right).
 \tag{2}
$$

If $0<\gamma\leq\gamma_\psi$, the spectral decomposition gives

$$
 \psi\leq O_\psi
 \leq\psi+(1-\gamma)(I-\psi).
$$

Therefore its expectation $\mu_\psi(\rho)=\operatorname{Tr}(O_\psi\rho)$ satisfies

$$
 F_\psi(\rho)
 \leq\mu_\psi(\rho)
 \leq 1-\gamma\,[1-F_\psi(\rho)].
 \tag{3}
$$

The good and bad promises are separated in this observable whenever

$$
 G:=\gamma\varepsilon_{\mathrm b}-\varepsilon_{\mathrm g}>0.
 \tag{4}
$$

In particular, exact-target certification works for every fixed $\varepsilon_{\mathrm b}\in(0,1)$. A robust example is $\varepsilon_{\mathrm g}=\gamma\varepsilon_{\mathrm b}/2$. The condition in (4) is part of the sufficient theorem: the argument does not claim to certify every arbitrarily prescribed pair of tolerant fidelity thresholds.

## 3. A bounded score using nonadaptive local measurements

Independently select $\theta_i$ uniformly from $\{X,Y,Z\}$ on every qubit and perform all selected measurements once. This can be done in parallel. Let $x=(x_A,x_B)$ denote the true outcome string, and put

$$
 P_{\theta_A,x_A}
 =|x_{A,\theta_A}\rangle\langle x_{A,\theta_A}|.
$$

The ideal classical score is

$$
 g_\theta(x)
 =\operatorname{Tr}\!\left[
   T_{\theta_B,x_B}
   \bigl(3P_{\theta_A,x_A}-I_A\bigr)
 \right].
 \tag{5}
$$

Since the two eigenvalues of $3P-I$ are $2$ and $-1$, including the zero-weight convention above gives the uniform bound

$$
 -1\leq g_\theta(x)\leq2.
 \tag{6}
$$

To verify unbiasedness, condition on the basis and outcome on $B$. If the resulting input state on $A$ is $\sigma$, the average single-qubit reconstruction satisfies

$$
 \frac13\sum_{\theta_A\in\{X,Y,Z\}}
 \sum_{x_A=0}^1
 \operatorname{Tr}(P_{\theta_A,x_A}\sigma)
 \bigl(3P_{\theta_A,x_A}-I_A\bigr)
 =\sigma.
$$

For example, this follows by inserting the Bloch-vector expressions for $P$ and $\sigma$. Averaging the resulting conditional expectation over the outcomes and bases on $B$ proves

$$
 \mathbb E_{\theta,x\mid\rho}[g_\theta(x)]
 =\operatorname{Tr}(O_\psi\rho)
 =\mu_\psi(\rho).
 \tag{7}
$$

No physical measurement on $A$ depends on the outcomes on $B$. The conditional target state in (5) is used only in classical postprocessing. Thus the notation for a conditional state does not introduce measurement feedback or require retaining an unmeasured quantum subsystem.

## 4. Exact classical inversion of the detector channel

Write $s=1-2q>0$. For a single bit the detector matrix and its inverse are

$$
 K_q=
 \begin{pmatrix}1-q&q\\q&1-q\end{pmatrix},
 \qquad
 K_q^{-1}
 =\frac1s
 \begin{pmatrix}1-q&-q\\-q&1-q\end{pmatrix}.
 \tag{8}
$$

For each chosen basis pattern, define the corrected score on the reported string $y$ by

$$
 h_\theta(y)
 =\bigl[(K_q^{-1})^{\otimes n}g_\theta\bigr](y).
 \tag{9}
$$

Explicitly, with $d_H$ denoting Hamming distance,

$$
 h_\theta(y)
 =s^{-n}\sum_{x\in\{0,1\}^n}
   (1-q)^{n-d_H(x,y)}(-q)^{d_H(x,y)}g_\theta(x).
 \tag{10}
$$

Negative coefficients are weights in a classical estimator. They are not probabilities or physical inverse operations.

For fixed $\theta$, let $p_\theta$ be the ideal outcome distribution. The reported distribution is exactly $K_q^{\otimes n}p_\theta$. The matrix is symmetric, so

$$
 \mathbb E_{y\mid\theta,\rho}[h_\theta(y)]
 =g_\theta^{\mathsf T}
   (K_q^{-1})^{\otimes n}K_q^{\otimes n}p_\theta
 =g_\theta^{\mathsf T}p_\theta.
$$

Together with (7), this proves

$$
 \mathbb E_{\theta,y\mid\rho}[h_\theta(y)]
 =\mu_\psi(\rho).
 \tag{11}
$$

Each inverse row has absolute sum $s^{-n}$ and ordinary sum one. Apply the inverse to $g_\theta-1/2$, whose absolute value is at most $3/2$, to obtain

$$
 \left|h_\theta(y)-\frac12\right|
 \leq\frac32s^{-n}.
 \tag{12}
$$

Thus every corrected observation lies in a common interval of width $3s^{-n}$.

The inversion is valid because the same basis pattern defines all hypothetical strings in (10). For a protocol whose later physical basis depends on earlier corrupted reports, its ideal and reported record distributions need not be related by this fixed product matrix. Equations (9)–(11) make no such assertion about adaptive protocols. Adaptivity is permitted by the converse but is unnecessary for this sufficient construction.

## 5. Finite-sample certification theorem

**Theorem.** Suppose a target has a known lower bound $0<\gamma\leq\gamma_\psi$, the detector has known $0\leq q<1/2$, and the promises obey $G=\gamma\varepsilon_{\mathrm b}-\varepsilon_{\mathrm g}>0$. The nonadaptive protocol above achieves error at most $\alpha$ on each promise using

$$
 N\geq
 \left\lceil
 \frac{18\,(1-2q)^{-2n}}{G^2}
 \log\frac1\alpha
 \right\rceil
 \tag{13}
$$

independent copies.

**Proof.** Average the $N$ corrected scores to obtain $\widehat\mu$, and accept precisely when

$$
 \widehat\mu\geq
 t:=1-\frac{\varepsilon_{\mathrm g}
                    +\gamma\varepsilon_{\mathrm b}}2.
$$

Equation (3) puts every good input mean at or above $1-\varepsilon_{\mathrm g}=t+G/2$, and every bad input mean at or below $1-\gamma\varepsilon_{\mathrm b}=t-G/2$. By (12), Hoeffding's one-sided bound gives, under either promise,

$$
 \Pr[\text{incorrect decision}]
 \leq
 \exp\!\left[-\frac{N G^2}{18s^{-2n}}\right].
$$

The copy count in (13) makes this at most $\alpha$. The inequalities in (3) hold for every density operator, so soundness is uniform over the composite alternative. $\square$

For exact-target certification, set $\varepsilon_{\mathrm g}=0$ in (13). For robust completeness, any fixed $\varepsilon_{\mathrm g}<\gamma\varepsilon_{\mathrm b}$ is allowed. Also, if the preparation obeys $\tfrac12\|\rho-\psi\|_1\leq\varepsilon_{\mathrm g}$, then $F_\psi(\rho)\geq1-\varepsilon_{\mathrm g}$, so the same acceptance guarantee applies. Preparation deviations and detector noise enter different parts of the statement: the former specify which inputs are accepted, while the latter increase the sampling cost of an unbiased score.

The method also yields a confidence interval rather than a binary decision. With probability at least $1-\alpha$,

$$
 |\widehat\mu-\mu_\psi(\rho)|\leq
 r_N:=3s^{-n}\sqrt{\frac{\log(2/\alpha)}{2N}}.
$$

Consequently, a valid fidelity interval is

$$
 \max\!\left\{0,1-\frac{1-\widehat\mu+r_N}{\gamma}\right\}
 \leq F_\psi(\rho)
 \leq\min\{1,\widehat\mu+r_N\}.
 \tag{14}
$$

This interval estimates fidelity through the witness inequalities (3); it is not an assertion that $\mu_\psi(\rho)$ equals fidelity.

## 6. Necessity from the target-informed binary converse

Let

$$
 a_n=1-q_n,
 \qquad b_n=q_n^2+(1-q_n)^2,
 \qquad
 \eta_n=C\left[n b_n^{n/2}+n^2a_n^n\right],
 \quad C=1024.
 \tag{15}
$$

The [uniform concentration theorem](uniform-concentration.md) supplies a Haar event of probability at least $1-e^{-80n^2}$ on which every admissible normalized noisy product effect has likelihood ratio within $\eta_n$ of one. Its transcript consequence holds for arbitrary classical interleaving of copies with a deterministic copy cap. Testing $\psi$ against $\tau=I/2^n$, with both errors at most $\alpha$, requires

$$
 N\geq\frac{2(1-2\alpha)^2}{\eta_n^2}
 \geq
 \frac{(1-2\alpha)^2}{2C^2n^4b_n^n}.
 \tag{16}
$$

The second inequality uses $a_n\leq\sqrt{b_n}$. The first follows from a transcript relative-entropy bound $D(P_\psi\|P_\tau)\leq N\eta_n^2$ and Pinsker's inequality. In particular, arbitrary classical interleaving does not cost an additional factor of $n$ in (16).

Every fidelity certificate satisfying the promises in Section 1 is also such a binary test once $2^{-n}\leq1-\varepsilon_{\mathrm b}$: the target belongs to the accepted set and the maximally mixed state belongs to the rejected set. Therefore (16) is a lower bound for the composite certification task, regardless of how much classical target information the verifier uses.

For $0\leq q_n\leq1/2$,

$$
 b_n=1-2q_n(1-q_n)\leq e^{-q_n},
 \qquad a_n\leq e^{-q_n}.
$$

If $nq_n/\log n\to\infty$, equation (15) becomes smaller than every inverse polynomial, and (16) gives the explicit superpolynomial lower bound

$$
 N\geq
 \frac{(1-2\alpha)^2}{2C^2}
 \frac{e^{nq_n}}{n^4}.
 \tag{17}
$$

The more accurate expression (16) retains $b_n^{-n}$. No assumption that $q_n$ is bounded away from zero is used in this argument.

## 7. The polynomial-copy threshold

The imported Haar gap theorem means that there are universal constants $\gamma_0,c_0>0$ such that, for all sufficiently large $n$,

$$
 \Pr_{\psi\sim\mathrm{Haar}}
 [\gamma_\psi\geq\gamma_0]
 \geq1-e^{-c_0n}.
$$

Fix $\varepsilon_{\mathrm b}\in(0,1)$, $0\leq\varepsilon_{\mathrm g}<\gamma_0\varepsilon_{\mathrm b}$, and $0<\alpha<1/2$, all independent of $n$. For any prescribed detector sequence $q_n$, intersect this gap event with the converse event. The resulting target set has Haar probability at least

$$
 1-e^{-c_0n}-e^{-80n^2}.
$$

For targets in these sets, the following statements hold.

**Sufficiency.** If $nq_n=O(\log n)$, then $q_n\to0$ and

$$
 (1-2q_n)^{-2n}
 =\exp\!\left[4nq_n+O(nq_n^2)\right]
 =n^{O(1)}.
$$

Equation (13), with $\gamma=\gamma_0$, therefore gives a polynomial-copy certificate. More explicitly, if $nq_n\leq K\log n$, its noise factor is at most $n^{4K+o(1)}$. If $nq_n=O(1)$, this construction uses a constant number of copies for fixed promises and confidence.

**Necessity.** If $nq_n/\log n\to\infty$, every allowed certificate needs superpolynomially many copies by (17). More generally, if $nq_n/\log n$ is unbounded but oscillatory, the same obstruction holds along a subsequence: there can be no one polynomial that bounds the copy complexity for all sufficiently large $n$. This distinction is needed for a literal “if and only if” statement about arbitrary detector sequences.

Thus an asymptotically polynomial copy bound exists for this generic certification problem exactly when $nq_n=O(\log n)$. The statement applies in particular to exact-target versus constant-infidelity certification. Its robust version has the explicit gap-dependent promise in (4).

For fixed $q\in(0,1/2)$, the converse has exponential factor $b(q)^{-n}$, whereas the composite-task construction above has factor $(1-2q)^{-2n}$. These bounds establish the polynomial-versus-superpolynomial threshold; they do not establish a matching fixed-noise exponential rate for composite fidelity certification. The matching rate for the simpler binary promise is a separate result.

At $q=1/2$, every reported bit is independent of its true outcome. No allowed local protocol can distinguish the target from the maximally mixed state with nontrivial success. At $q=0$, the inverse is the identity and the constant-gap ideal certification guarantee is recovered.

## 8. Classical cost and scope

Evaluating (5) requires target-conditioned amplitudes. A direct evaluation of (10) uses all $2^n$ hypothetical outcome strings for the selected basis. Complete target information and unrestricted classical computation make this a valid sample-complexity protocol, but neither evaluation is claimed to be polynomial time for generic targets. The same distinction applies if the target is specified by a preparation circuit: its amplitudes may require exponential classical computation. The protocol invokes no quantum data-loading or QRAM primitive.

Exact knowledge of the detector channel is used in (8). If an implementation approximates the ideal score uniformly to error $\zeta$, inversion can amplify that deterministic error to at most $s^{-n}\zeta$. Such error must fit inside the decision margin $G/2$; it cannot be absorbed into the statistical confidence without accounting for it.

The sufficient theorem is target-specific whenever a positive gap bound is available. The Haar theorem supplies a large class of such targets. No constant gap is asserted for every pure state, and no general design-to-gap transfer is assumed here. The universal local-detection converse and the sufficient certificate are both stated for independent copies of a fixed source state and the specified known, independent binary readout noise.

## Primary source

Zhenyu Du, Jinchang Liu, Elias X. Huber, Zi-Wen Liu, and Xiongfeng Ma, *Certifying localizable quantum properties with constant sample complexity*, arXiv:2509.17580v3 (20 July 2026), published in Physical Review X 16, 041027 (2026). The precise imported results are Eq. (33), Proposition 5 and Eq. (35), Theorem 5, Appendix A.1 Eq. (A2) and Corollary S1, and Appendix F.1. [Full primary text](https://arxiv.org/html/2509.17580v3) · [Published article](https://journals.aps.org/prx/abstract/10.1103/rkl6-hfrn).
