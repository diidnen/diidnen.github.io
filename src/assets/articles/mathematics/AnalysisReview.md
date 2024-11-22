# Analysis Review

Suppose that $|f(z)| \leq M$ for all $z$ on the path $\gamma$. Then

$$\left|\int_\gamma f(z)dz\right| \leq ML(\gamma)$$


$f$ be a function which is continuous throughout a domain $D$ is quite important 

**Theorem** (Antiderivative Theorem). Let $\Omega$ be a convex domain(i.e. a domain in which any two points can be joined by a line segment) and let $f$ be continuous on $\Omega$, and that

$$\int_\gamma f(z)dz = 0 \tag{5.1}$$

for any triangular contour $\gamma$ such that $\gamma^* \subset \Omega$. Then for any point $a \in \Omega$ the function

$$F(z) = \int_{[a,z]} f(w)dw$$

is a primitive of $f$ on $\Omega$.


**Cauchy Theorem**: Let $f$ be analytic in a domain $D$ and let $\gamma$ be a closed contour lying in $D$. Then

$$\int_\gamma f(z)dz = 0$$

We can also rephrase this theorem as: holds for any contour $\gamma \subset \Omega$ if the domain $\Omega$ is simply connected.
(simply connected means that the domain has no holes and also the contour does not intersect itself)

domain definition: A domain is a connected open set.

**Lemma** (The Keyhole Lemma). Let $f \in H(\Omega)$ with a domain $\Omega$. Let $\gamma_1$, $\gamma_2$ be positively oriented contours in $\Omega$ such that $\operatorname{Int}(\gamma_1) \subset \operatorname{Int}(\gamma_2)$ and $\operatorname{Ext}(\gamma_1) \cap \operatorname{Int}(\gamma_2) \subset \Omega$. Then

$\int_{\gamma_1} f(z)dz = \int_{\gamma_2} f(z)dz$
(easy to transform some integrals into easier integrals)


Cauchy Theorem for a triangle: Let $f$ be analytic in a domain $\Omega$ and let $\triangle$ be a triangle in $\Omega$. Then

$\int_\triangle f(z)dz = 0$  


**Cauchy Integral Formula**: Let $f$ be holomorphic on a domain $\Omega$(simply connected) and let $\gamma$ be a closed contour in $\Omega$. Then

$$\int_\gamma \frac{f(z)}{z-a}dz = 2\pi i f(a)$$

for any point $a$ inside $\gamma$.   

notion:(we need to satisfy the condition that the the function in the chosen domain is holomorphic, for example, the function $f(z) = \frac{1}{z}$ is not holomorphic on the domain that contains the origin, so we cannot use the Cauchy Integral Formula on the origin, also $f(z) = \frac{cosz}{1+z^2}$ is not holomorphic on the domain that contains the point $z = i$(disk D(2i,0)), so if we cannot use the Cauchy Integral Formula in that domain, we need to find other methods to solve the problem,like trying to deal with the function into another form that can make the function to be holomorphic on the domain)
他的点一定要在interior里面
**Cauchy Integral Formula for Derivatives**: Let $f$ be holomorphic on a domain $\Omega$(simply connected) and let $\gamma$ be a closed contour in $\Omega$. Then

$$f^{(n)}(a) = \frac{n!}{2 \pi i} \int_\gamma \frac{f(z)}{(z-a)^{n+1}}dz$$

for any point $a$ inside $\gamma$.  (be careful with the power of the denominator to have power $n+1$)

Morera's Theorem:
Let $f$ be continuous on a domain $\Omega$ and that

$$\int_\gamma f(z)dz = 0$$

for any triangular contour $\gamma \subset \Omega$. Then $f$ is holomorphic on $\Omega$.


**Cauchy's Estimate**: Let $f$ be holomorphic on a domain $\Omega$ and let $D(a,r)$ be a disk(it can have boudary) in $\Omega$. Then

$$|f^{(n)}(a)| \leq \frac{n!M}{r^n}$$

for any $M > 0$ such that $|f(z)| \leq M$ for all $z \in D(a,r)$.

**Liouville's Theorem**: Let $f$ be entire and bounded(i.e. $|f(z)| \leq M$ for all $z \in \mathbb{C}$). Then $f$ is constant.

Let $p(z)$ be a non-constant polynomial. Then $p(z)$ has a root in $\mathbb{C}$.

any polynomial of degree $n$ has $n$ roots in $\mathbb{C}$
感觉现在modulus有点问题

**Uniform Convergence**:
we now consider the convergence of a sequence of functions $f_n(z)$ to a function $f(z)$ on a domain $\Omega$.

we say this sequence converges pointwise to another function $f$ on $\Omega$ if for every $\epsilon > 0$, there exists an integer $N$ such that

$$|f_n(z) - f(z)| < \epsilon$$

for all $z \in \Omega$ and for all $n \geq N$.

we say this sequence converges uniformly to another funtion $f$ if sup$|f_n(z) - f(z)| \to 0$ as $n \to \infty$ uniformly on $\Omega$.

the uniformity emphasizes that the same $N$ works for all $z \in \Omega$.

the uniform convergence can be rephrased by saying the sequence a_n=sup|f_n(z)-f(z)| converges to 0 as $n \to \infty$（where z is in $\Omega$
uniform convergence is implies pointwise convergence.

也就是我要定义两个东西第一个逼近的函数，第二个是找到一个domain，在这个domain上，这个函数和逼近的函数之间的差值小于一个很小的数。也就是pointwise convergence。这个N取决于（z和$\epsilon$）

uniform convergence是说，这个N只取决于$\epsilon$，和z无关。因为我这里描述的是sup($z \in \Omega$)||f_n(z)-f(z)||,每次都是取得最大的那么一个值

就相当于我的uniform convergence要保证对于 $\forall z \in \Omega$, 存在一个N，使得都converge，而不是对于特定的z我存在一个不同的N。

uniform convergence of series: we say that the series $\sum_{n=1}^{\infty} f_n(z)$ converges uniformly on $\Omega$ if the sequence of partial sums $s_n(z) = \sum_{k=1}^{n} f_k(z)$ converges uniformly on $\Omega$.(这是一个definition就是描述说我们怎么定义一个series的uniform convergence)

这样的话我们可以定义uniform convergence sequences的计算 limit和integration因为每一个N都是一样的。

let $\gamma$ be a contour in $\Omega$,$lim_{n \to \infty} \int_\gamma f_n(z)dz = \int_\gamma lim_{n \to \infty} f_n(z)dz = \int_\gamma f(z)dz$

好现在就要引入说既然我们已经有了这么多性质，我们要怎么证明一个series converge uniformly。

**Weierstrass M-test**: suppose that $f_n$ is a sequence of functions on $\Omega$ and that there exists a sequence of positive numbers $M_n$ such that

$$|f_n(z)| \leq M_n$$

for all $z \in \Omega$ and for all $n \geq 1$. If $\sum_{n=1}^{\infty} M_n$ converges, then $\sum_{n=1}^{\infty} f_n(z)$ converges uniformly on $\Omega$.

**Taylor's Theorem**: Let $f$ be analytic on a domain $\Omega$ and let $D(a,r)$ be a disk in $\Omega$. Then for any $z_0 \in D(a,r)$

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(z-a)^n$$

for all $z \in D(a,r)$.
 
and notice that the radius of convergence of the of $f(z)$ is the same as the radius of convergence of $f'(z)$ .

其实这里比较重要的一点就是$f(z)$ \in H(D(z_0,r))$,with r>0, then at each point $z \in D(z_0,r)$, $f$ has a power series representation
我必须要让f在$D(z_0,r)$上analytic，然后我才能用泰勒定理，而且选的点$z_0$必须在$D(z_0,r)$上。


**Theorem 5.31**: Suppose that $f$ is an entire function and that there are numbers $M$ and $R$ such that $|f(z)| \leq M |z|^n$ for all $|z| \geq R$. Then $f$ is a polynomial of degree at most $n$.
定义两个东西一个是$M$，一个是$R$，然后$M$是一个常数，$R$是$z$的radius of convergence。


Laurent expansion: if a function fails to be analytic at a point $a$, we can still represent it as a power series, but it will have negative power terms.

and the coefficients of every term can be calculated by the formula

$$c_n = \frac{1}{2\pi i} \int_\gamma \frac{f(z)}{(z-a)^{n+1}}dz$$

where $\gamma$ is a closed contour around $a$.

**Lemma 6.2**. Let $f \in H(\Omega)$ with a domain $\Omega$ and let $\gamma_1$ and $\gamma_2$    be closed contours in $\Omega$ such that $\operatorname{Int}(\gamma_1) \subset \operatorname{Int}(\gamma_2)$ and $\operatorname{Ext}(\gamma_1) \cap \operatorname{Int}(\gamma_2) \subset \Omega$. Then for any $z \in \operatorname{Int}(\gamma_1)\cap \operatorname{Int}(\gamma_2)$ the formulae holds:

$$f(z) = \frac{1}{2\pi i} \int_{\gamma_1} \frac{f(w)}{w-z}dw - \frac{1}{2\pi i} \int_{\gamma_2} \frac{f(w)}{w-z}dw$$


**Cauchy's inequalities for the laurent series**: let $f$ be analytic on an annulus $A(a,r_1,r_2)$ and let $M(r)$ be the maximum value of $|f(z)|$ on $r_1<r<r_2$. Then

$$|a_n| \leq \frac{M(r)}{r^n}$$

for all $n \geq 0$ and all $r$ such that $r_1 \leq r \leq r_2$.(就是一个来找laurent expansion系数的) 

可以证明如果被bounded那么就是constant

a point $a$ is an isolated singularity of $f$ if there exists a punctured disk $D(a,\epsilon)$ such that $f$ is analytic on $D(a,\epsilon) \setminus \{a\}$.
(isolated singularity就是说他周围有一个小洞，然后这个洞里面没有其他的奇点)
$\frac{1}{\sin(\frac{\pi}{z})}$是一个有趣的函数 他除了z=0以外存在的singular point 都是isolated singularity但是对于z=0他不是isolated singularity？？

**Definition 6.6**: let $a$ be an isolated singularity of $f$. The residue of $f$ at $a$, denoted by $\operatorname{Res}(f,a)$, is the coefficient $c_{-1}$ in the Laurent expansion of $f$ at $a$:

$$f(z) = \sum_{n=-\infty}^{\infty} c_n (z-a)^n$$    
notes说这个很特么有用，接着往下看吧 </br>

**Cauchy's Residue Theorem**: let $f$ be analytic on an annlus $A(a,r_1,r_2)$ except for finitely many isolated singularities $a_1,a_2,...,a_N$ at $a$. Let $\gamma$ be a closed contour in $A(a,r_1,r_2)$ that contains $a$ in its interior and suppose that $\gamma$ is positively oriented. Then

$$\int_\gamma f(z)dz = 2\pi i \sum_{k=1}^{N} \operatorname{Res}(f,a_k)$$

(注意这里一定要是isolated singularities)

这里的contour必须是一个positively oriented的contour，并且包含$a_k$，而且$a_k$是contour内部唯一的singularity。


