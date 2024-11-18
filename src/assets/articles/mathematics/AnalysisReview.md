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

$$\int_{\gamma_1} f(z)dz = \int_{\gamma_2} f(z)dz.$$(easy to transform some integrals into easier integrals)


Cauchy Theorem for a triangle: Let $f$ be analytic in a domain $\Omega$ and let $\triangle$ be a triangle in $\Omega$. Then

$$\int_\triangle f(z)dz = 0$$   


**Cauchy Integral Formula**: Let $f$ be holomorphic on a domain $\Omega$(simply connected) and let $\gamma$ be a closed contour in $\Omega$. Then

$$\int_\gamma \frac{f(z)}{z-a}dz = 2\pi i f(a)$$

for any point $a$ inside $\gamma$.   

notion:(we need to satisfy the condition that the the function in the chosen domain is holomorphic, for example, the function $f(z) = \frac{1}{z}$ is not holomorphic on the domain that contains the origin, so we cannot use the Cauchy Integral Formula on the origin, also $f(z) = \frac{cosz}{1+z^2}$ is not holomorphic on the domain that contains the point $z = i$(disk D(2i,0)), so if we cannot use the Cauchy Integral Formula in that domain, we need to find other methods to solve the problem,like trying to deal with the function into another form that can make the function to be holomorphic on the domain)

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
