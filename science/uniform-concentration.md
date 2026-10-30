# Uniform concentration of noisy product effects

This chapter proves a simultaneous likelihood bound for all noisy single-qubit product effects of a Haar-random target. The simultaneous quantifier is essential: the target may be known before the measurement axes, qubit order, or feedback rule are chosen. The bound also covers partial measurement records. Its application to protocols that interleave measurements of different copies is proved in [the binary sample law](binary-sample-law.md).

All logarithms are natural. A pure state is identified with its rank-one density operator when it appears inside a trace.

## 1. Statement and notation

Let

```math
n\geq 1,\qquad d=2^n,\qquad 0\leq q\leq \frac12,
```

and define

```math
s=1-2q,\qquad a=1-q=\frac{1+s}{2},\qquad
b=(1-q)^2+q^2=\frac{1+s^2}{2}.
```

For a unit Bloch vector $`u\in S^2`$, put

```math
F_s(u)=\frac{I+s\,u\cdot\sigma}{2}.
```

This is the effect of one specified reported outcome of a rank-one qubit projective measurement whose ideal outcome is independently flipped with probability $`q`$. Its eigenvalues are $`a`$ and $`q`$, and its trace is one.

For $`u=(u_1,\ldots,u_n)\in(S^2)^n`$, define the normalized product effect

```math
E_s(u)=\bigotimes_{j=1}^n F_s(u_j).
```

If $`\psi`$ is a unit vector, write

```math
L_\psi(E)=d\langle\psi|E|\psi\rangle,
\qquad r_\psi(E)=L_\psi(E)-1.
```

For an effect of trace one, $`L_\psi(E)`$ is the ratio of its probability on $`\psi`$ to its probability on $`I/d`$.

### Theorem 1. Uniform noisy-product bound

The universal constant

```math
C_{\mathrm{unif}}=1024
```

is sufficient for the following statement. For every $`n\geq1`$ and every prescribed $`q\in[0,1/2]`$, set

```math
\boxed{\quad
\delta_n(q)=C_{\mathrm{unif}}
\left[n\,b^{n/2}+n^2a^n\right].
\quad} \tag{1}
```

With probability at least $`1-\exp(-80n^2)`$ over Haar-random $`\psi`$,

```math
\boxed{\quad
\sup_{u\in(S^2)^n}
\left|d\langle\psi|E_s(u)|\psi\rangle-1\right|
\leq\delta_n(q).
\quad} \tag{2}
```

The same event gives (2) for every product whose local factors are
$`F_s(w_j)=(I+s\,w_j\cdot\sigma)/2`$ with $`\|w_j\|_2\leq1`$, and for every convex combination of these products.

The numerical constants are deliberately conservative. They establish a finite-dimensional statement with constants independent of $`n`$ and $`q`$. The error probability is over the target alone. Once the event holds, the axes and their selection rules may depend arbitrarily on that target.

## 2. A normalized Gaussian moment bound

The required fixed-effect concentration follows from a scalar calculation. Keeping the Gaussian normalization exact avoids an additional exceptional event.

### Lemma 2. Moments of a centered Haar quadratic form

Let $`A`$ be a traceless Hermitian $`d\times d`$ matrix, and put

```math
v=\mathrm{tr}(A^2),\qquad \ell=\|A\|_\infty.
```

For every integer $`k\geq1`$ and Haar-random unit vector $`\psi`$,

```math
\begin{gathered}
\left(\mathbb E
\left|d\langle\psi|A|\psi\rangle\right|^{2k}\right)^{1/(2k)}
\leq 2\sqrt{k v}+3k\ell.
\end{gathered} \tag{3}
```

#### Proof

Take a standard complex Gaussian vector $`g\in\mathbb C^d`$, with independent coordinates of density $`\pi^{-1}e^{-|z|^2}`$. The variables $`|g_j|^2`$ are independent exponentials of mean one. If

```math
G=\|g\|_2^2,\qquad \psi=g/\sqrt G,
```

then $`\psi`$ is Haar-random, $`G`$ has the gamma distribution of shape $`d`$ and scale one, and $`G`$ is independent of $`\psi`$.

Let $`X=g^*Ag`$. Diagonalizing $`A`$, with real eigenvalues $`\lambda_1,\ldots,\lambda_d`$, gives

```math
X=\sum_{j=1}^d\lambda_j(Y_j-1),
```

where the $`Y_j`$ are independent mean-one exponential variables; the centering uses $`\sum_j\lambda_j=0`$. For $`|t|\ell\lt 1`$,

```math
\begin{aligned}
\log\mathbb E e^{tX}
&=\sum_j\left[-t\lambda_j-\log(1-t\lambda_j)\right]\\
&=\sum_j\sum_{m\geq2}\frac{(t\lambda_j)^m}{m}\\
&\leq\frac{v t^2}{2(1-|t|\ell)}.
\end{aligned} \tag{4}
```

Applying Chernoff's inequality to $`X`$ and $`-X`$ yields

```math
\begin{gathered}
\Pr\left\{|X|\geq\sqrt{2vx}+\ell x\right\}
\leq 2e^{-x},\qquad x\geq0.
\end{gathered} \tag{5}
```

For completeness, when $`v>0`$, the upper-tail bound follows by choosing
$`t=\sqrt{2x/v}/(1+\ell\sqrt{2x/v})`$ in (4); the lower tail uses the same choice for $`-X`$. If $`v=0`$, then $`A=0`$ and the conclusion is immediate.

Let $`Z=\log2+Y`$, where $`Y`$ is a mean-one exponential variable. Inequality (5) says that $`|X|`$ is stochastically dominated by $`\sqrt{2vZ}+\ell Z`$. Minkowski's inequality therefore gives

```math
\|X\|_{2k}
\leq\sqrt{2v}\,\|Z\|_k^{1/2}+\ell\|Z\|_{2k}.
```

Since $`\|Y\|_m=(m!)^{1/m}\leq m`$ for an integer $`m\geq1`$,

```math
\|Z\|_k\leq k+\log2\leq2k,
\qquad
\|Z\|_{2k}\leq2k+\log2\leq3k.
```

Consequently,

```math
\begin{gathered}
\|X\|_{2k}\leq2\sqrt{k v}+3k\ell.
\end{gathered} \tag{6}
```

Finally, set $`r=d\langle\psi|A|\psi\rangle`$. Radial independence gives

```math
\begin{gathered}
X=(G/d)r,
\qquad
\mathbb E|X|^{2k}
=\frac{(d)_{2k}}{d^{2k}}\,\mathbb E|r|^{2k},
\end{gathered} \tag{7}
```

where $`(d)_m=d(d+1)\cdots(d+m-1)`$. The factor $`(d)_{2k}/d^{2k}`$ is at least one. Thus $`\|r\|_{2k}\leq\|X\|_{2k}`$, proving (3). $`\square`$

### Corollary 3. Moments for one noisy product effect

For every $`u\in(S^2)^n`$ and integer $`k\geq1`$,

```math
\boxed{\quad
\|r_\psi(E_s(u))\|_{2k}
\leq2\sqrt{k\left(b^n-d^{-1}\right)}
+3k\left(a^n-d^{-1}\right)
\leq3\left(\sqrt{k}\,b^{n/2}+k a^n\right).
\quad} \tag{8}
```

#### Proof

The matrix $`A=E_s(u)-I/d`$ is traceless. Tensor products give

```math
\begin{gathered}
\mathrm{tr}(E_s(u)^2)=b^n,
\qquad
\mathrm{tr}(A^2)=b^n-d^{-1}.
\end{gathered} \tag{9}
```

The largest and smallest eigenvalues of $`E_s(u)`$ are $`a^n`$ and $`q^n`$. Moreover,

```math
a^n+q^n\geq2\left(\frac{a+q}{2}\right)^n=2d^{-1},
```

by convexity of $`x\mapsto x^n`$. Hence

```math
\begin{gathered}
\|E_s(u)-I/d\|_\infty=a^n-d^{-1}.
\end{gathered} \tag{10}
```

Apply Lemma 2. $`\square`$

Equation (8) retains both the quadratic and linear Bernstein scales. In particular, it does not assume that $`q`$ is a positive constant as $`n`$ grows.

## 3. The product net and proof of Theorem 1

Set

```math
\eta_n=\frac{1}{4n4^n}.
```

There is an $`\eta_n`$-net $`\mathcal N_n`$ of the unit sphere $`S^2`$, in Euclidean distance, with

```math
|\mathcal N_n|\leq(1+2/\eta_n)^3.
```

Indeed, take a maximal $`\eta_n`$-separated subset of $`S^2`$. The balls of radius $`\eta_n/2`$ centered at its points are disjoint and lie inside the ball of radius $`1+\eta_n/2`$ in $`\mathbb R^3`$, giving the displayed volume bound. Maximality gives the covering property.

The product net has size

```math
\begin{aligned}
\log|\mathcal N_n^n|
&\leq3n\log(1+8n4^n)\\
&\leq3n\left(\log9+\log n+2n\log2\right)\\
&\leq14n^2.
\end{aligned} \tag{11}
```

The final inequality holds for every $`n\geq1`$, using $`\log n\leq n`$.

Write

```math
A_n=n b^{n/2}+n^2a^n,
```

so that $`\delta_n=1024A_n`$. Choose the integer $`k=32n^2`$. For each fixed point of the product net, the sharper first bound in (8) implies

```math
\|r_\psi(E)\|_{2k}
\leq2\sqrt{32}\,n b^{n/2}+96n^2a^n
\leq96A_n.
```

Markov's inequality therefore gives

```math
\begin{gathered}
\Pr\left\{|r_\psi(E)|>\delta_n/2\right\}
\leq\left(\frac{96}{512}\right)^{64n^2}
=\left(\frac{3}{16}\right)^{64n^2}.
\end{gathered} \tag{12}
```

Combining (11) and (12), with no independence assumption between net points, bounds the probability of failure anywhere on the net by

```math
\begin{gathered}
\exp\left[-\left(64\log(16/3)-14\right)n^2\right]
\leq e^{-80n^2}.
\end{gathered} \tag{13}
```

It remains to extend from the net to all axes. If $`\|u_j-v_j\|_2\leq\eta_n`$ for every site, then

```math
\|F_s(u_j)-F_s(v_j)\|_\infty
=\frac{s}{2}\|u_j-v_j\|_2\leq\frac{\eta_n}{2}.
```

A telescoping expansion of the tensor products, using $`\|F_s(u_j)\|_\infty\leq1`$, gives

```math
\|E_s(u)-E_s(v)\|_\infty\leq\frac{n\eta_n}{2}.
```

Thus, for every unit vector $`\psi`$,

```math
\begin{gathered}
|r_\psi(E_s(u))-r_\psi(E_s(v))|
\leq\frac{dn\eta_n}{2}=\frac{2^{-n}}8.
\end{gathered} \tag{14}
```

Because $`b\geq1/2`$,

```math
\frac{2^{-n}}8\leq\frac{\delta_n}{2}.
```

On the event that all net values have absolute value at most $`\delta_n/2`$, (14) consequently gives (2) for every product effect.

To obtain the Bloch-ball extension, write a vector $`w`$ of length $`r\leq1`$ as $`w=r u`$, choosing any $`u\in S^2`$ if $`w=0`$. Then

```math
\begin{gathered}
F_s(w)=\frac{1+r}{2}F_s(u)+\frac{1-r}{2}F_s(-u).
\end{gathered} \tag{15}
```

Taking tensor products expresses every Bloch-ball product as a convex combination of sphere products. The map $`E\mapsto r_\psi(E)`$ is affine on trace-one matrices, so its absolute value remains at most $`\delta_n`$ under this convexification. A further convex combination has the same property. This completes the proof of Theorem 1. $`\square`$

## 4. Partial measurement records

Suppose a subset $`J\subseteq\{1,\ldots,n\}`$ of one input copy has been measured. On a fixed recorded branch, let $`u_j`$ denote the signed axis associated with the reported outcome at site $`j`$. The unnormalized effect of this partial record is

```math
H_J=
\bigotimes_{j\in J}F_s(u_j)
\otimes\bigotimes_{j\notin J}I.
```

Its trace is $`2^{n-|J|}`$. Its trace-one normalization is therefore

```math
\begin{gathered}
\overline H_J=
\bigotimes_{j\in J}F_s(u_j)
\otimes\bigotimes_{j\notin J}\frac I2.
\end{gathered} \tag{16}
```

The unread sites in (16) have zero Bloch vector and are covered by (15). On the event in Theorem 1,

```math
\begin{gathered}
\left|
\frac{\mathrm{tr}(\psi H_J)}
{\mathrm{tr}((I/d)H_J)}-1
\right|
=\left|d\mathrm{tr}(\psi\overline H_J)-1\right|
\leq\delta_n.
\end{gathered} \tag{17}
```

This includes the empty record, whose likelihood ratio is exactly one. The bound remains valid when the subset, axes, and reported branch were selected using the target and all earlier classical records. The theorem controls all such normalized effects simultaneously.

## 5. Fixed and vanishing readout noise

Two consequences of the finite-dimensional bound will be used below.

First, for fixed $`0\lt q\lt 1/2`$,

```math
\begin{gathered}
a^2\lt b,
\qquad
\delta_n(q)
=C_{\mathrm{unif}}\,n b^{n/2}
\left[1+n\left(\frac a{\sqrt b}\right)^n\right]
=C_{\mathrm{unif}}\,n b^{n/2}(1+o(1)).
\end{gathered} \tag{18}
```

Discarding the second term is an asymptotic step, not part of Theorem 1.

Second, for any prescribed sequence $`q=q_n\in[0,1/2]`$,

```math
\begin{aligned}
\delta_n(q_n)
&\leq2C_{\mathrm{unif}}n^2 b_n^{n/2}\\
&\leq2C_{\mathrm{unif}}n^2
\exp[-nq_n(1-q_n)]\\
&\leq2C_{\mathrm{unif}}n^2\exp[-nq_n/2].
\end{aligned} \tag{19}
```

Here $`a_n^2\leq b_n`$, $`1-x\leq e^{-x}`$, and $`q_n\leq1/2`$ were used. In particular, if $`nq_n/\log n\to\infty`$, then $`\delta_n`$ is smaller than every inverse polynomial. This conclusion retains both Bernstein terms and does not require fixed positive noise.

At $`q=1/2`$, every local factor is exactly $`I/2`$, so every likelihood ratio in (2) equals one. At $`q=0`$, the uniform theorem is still valid, but its bound does not tend to zero.

## References and relation to existing bounds

The Gaussian estimates above are proved directly. The use of high moments and a product-state net follows established concentration methods. In particular, [Low, Theorem 6.4](https://arxiv.org/pdf/0903.5236) proves uniform product-overlap concentration for approximate state designs; the same paper's Theorem 1.2 provides a general moment-transfer method.

The fixed-effect Hilbert–Schmidt quantity in (9), and the resulting readout-flattening scale $`b^{n/2}`$, already occur in [Maciejewski, Puchała and Oszmaniec, *Operational Quantum Average-Case Distances*, Example 2](https://quantum-journal.org/papers/q-2023-09-11-1106/pdf/) and their companion [*Exploring Quantum Average-Case Distances: proofs, properties, and examples*, Example 10, Eq. (132)](https://arxiv.org/html/2112.14284v6). The statement needed here is simultaneous over target-dependent product effects; the sample-complexity consequence additionally requires control of complete adaptive transcripts.
