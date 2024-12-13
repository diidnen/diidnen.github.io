# Analysis Review

verify Cauchy_Riemann equations:

$$u_x = v_y, u_y = -v_x$$

and if it is asked to prove by definition, we approch $z_0$ as a point on the curve horisontally and vertically.

harmonic conjugate:

sheet 2 question 5 没看懂为什么不可以直接用Cauchy Riemann equations来证明。

**Definition 2.6.** Let $z_1, z_2 \in \mathbb{C}$. Then the set
$$[z_1,z_2] = \{z = (1 - \alpha)z_1 + \alpha z_2 \mid \alpha \in [0,1]\}$$
is called the segment joining $z_1$ and $z_2$.

Assume that $u, v$ have continuous second order derivatives:
$$u_{xx}, u_{xy} = u_{yx}, u_{yy}, v_{xx}, v_{xy} = v_{yx}, v_{yy}$$

Differentiate CRE:
$$u_{xx} = v_{yx}, \quad u_{yy} = -v_{xy} = -v_{yx}$$

Add up:
$$\Delta u = u_{xx} + u_{yy} = 0$$

Laplace operator. In the same way $\Delta v = 0$

**Definition 2.9.** If $u$ has continuous partial derivatives of first and second order, and $\Delta u = 0$, then $u$ is said to be a harmonic function.

**Definition 2.10.** An ordered pair $(u, v)$ of harmonic functions $u$ and $v$ on $\Omega$ are called harmonic conjugates if $u + iv$ is holomorphic on $\Omega$.

注意continuous为了满足lim

Let $g: \mathbb{R}^2 \to \mathbb{R}$ be harmonic and assume that all its second partial derivatives exist and are continuous. Show that the function $f$ defined by
$$f = \frac{\partial g}{\partial x} - i\frac{\partial g}{\partial y}$$
is holomorphic.

**Solution:** From a theorem in class, a set of conditions on $u$, $v$, and their derivatives under which $f$ is holomorphic at $z_0$ are the following:

- $u$, $v$ are continuous on $D$
- $\frac{\partial u}{\partial x}$, $\frac{\partial u}{\partial y}$, $\frac{\partial v}{\partial x}$, $\frac{\partial v}{\partial y}$ exist on $D$ and are continuous at $z_0 = (x_0, y_0)$
- The Cauchy-Riemann equations hold:
  $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

We check the conditions for $f$. We have $f = u + iv$ with
$$u = \frac{\partial g}{\partial x}, \quad v = -\frac{\partial g}{\partial y}$$

Since the partial derivatives of $g$ are continuous, $u$ and $v$ are continuous. The partial derivatives of $u$ and $v$ exist and are:
$$\frac{\partial u}{\partial x} = \frac{\partial^2 g}{\partial x^2}, \quad 
\frac{\partial u}{\partial y} = \frac{\partial^2 g}{\partial x\partial y}, \quad
\frac{\partial v}{\partial x} = -\frac{\partial^2 g}{\partial y\partial x}, \quad
\frac{\partial v}{\partial y} = -\frac{\partial^2 g}{\partial y^2}$$
这里很重要一定要check

As the second partials of $g$ are continuous at $(x_0, y_0)$, the first partial derivatives of $u$ and $v$ are continuous at $(x_0, y_0)$. Now we check the Cauchy-Riemann equations for $u$ and $v$:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \iff 
\frac{\partial^2 g}{\partial x^2} = -\frac{\partial^2 g}{\partial y^2} \iff
\frac{\partial^2 g}{\partial x^2} + \frac{\partial^2 g}{\partial y^2} = \Delta g = 0$$

which holds, as $g$ is harmonic.

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \iff
\frac{\partial^2 g}{\partial x\partial y} = -\left(-\frac{\partial^2 g}{\partial y\partial x}\right) =
\frac{\partial^2 g}{\partial y\partial x}$$

which holds, as the mixed partial derivatives of $g$ are equal.

holomorphic等价于power series converge在于其实holomorphic想描述的就是每一次的differivative都存在，然后由于power series的收敛半径和differivative的收敛半径是一样的，所以我们可以用power series来描述holomorphic。

几个Important的inequality $Re(z) \leq |z|, Im(z) \leq |z|$, $|z+w| \leq |z|+|w|$ $|z+w| \leq ||z|-|w||$

A sequence {zn} is said to be a Cauchy sequence (or Cauchy), if for every ε > 0 there is a
number N = Nε > 0 such that $|z_n-z_m|<\epsilon$ for all $n,m \geq N$

Proposition 1.8. zn → w iff Re zn → Rew, Im zn → Im w.
If zn → w, then zn → w and |zn| → |w|.
A sequence {zn} converges iff it is Cauchy.(注意这里定义的逼近是实数项和虚数项一起逼近，也就是说我们所谓的复数趋近其实描述的是实数项和虚数项的趋近)

**Definition 1.9.** Let $z_0$ be a complex number and $r > 0$ be a real number. Then the set
$S (z_0,r) = {z : |z − z_0| = r} = {z = z_0 + r e^{i\phi}, \phi \in (-\pi,\pi]}$
is called circle centered at $z_0 \in \mathbb{C}$ of radius $r > 0$. The set
$D(z_0,r) = {z \in \mathbb{C} | |z - z_0| < r}$
is called an r-neighbourhood of $z_0$ or an open disk of radius $r$ centered at $z_0$. The set
$D(z_0,r) = {z \in \mathbb{C} | |z - z_0| \leq r}$
is called the closed disk of radius $r$ centered at $z_0$.
The set
$D'(z_0,r) = {z \in \mathbb{C} : 0 < |z - z_0| < r}$
is called a punctured r-neighbourhood of $z_0$.

The set $S$ is said to be convex if for any two points $z_1, z_2 \in S$, the segment $[z_1,z_2]$ also belongs to $S$.

a set S is connected if for every two points $z,w \in S$ there exists a polygonal path joing them and lying within S!!

but we define simply connected by if for any contour $\gamma \in \omega$ we have $wInt(\gamma) \subset \omega$

convex：任意两点之间的连线都在这个区域内


interior point is defined by as having a circle centered at the point, and there exist a radius $r$ such that all the points inside the circle belong to the set. which is $D(z_0,r)$

And the set is open if every point is an interior point.

complex function 要well defined，以及我们一般是定义在domain上，也就是open connected set，以及这个complex function is hard to visualize,但是我们可以把它看作一个transformation，也就是把一个点映射到另一个点或者另外一个值(e.g. $f(z) =arg(z)$ 像这个函数在负半轴就不存在，因为对于一个在负半轴上的点，如果我们画一个小圆，从上面和下面趋近的值不一样，因为我们定义的arg$\theta$是$(-\pi,\pi]$，所以从上面趋近和下面趋近的值不一样)。

总感觉趋近可以考虑一个centered at the point的circle，然后看这个circle上的点趋近到这个点的时候，函数的值趋近到哪里。

Suppose that $|f(z)| \leq M$ for all $z$ on the path $\gamma$. Then

$$\left|\int_\gamma f(z)dz\right| \leq ML(\gamma)$$

(suppose that $|f(z)| \leq M$ for all $z$ on the path $\gamma$,也就是这是考虑path的bound)

$f$ be a function which is continuous throughout a domain $D$ is quite important 
A set $S \subset \mathbb{C}$ is said to be convex if for every two points $z_1,z_2 \in S$ the segment $[z_1,z_2]$ also belongs to $S$.

We say that a set $S$ is polygonally connected (or, simply, connected) if for every two points $z,w \in S$ there exists a polygonal path joining them and lying within $S$.

Any open connected set is called domain or region.

Theorem 2.9. Let Ω be a domain. Suppose that f ∈ H(Ω).
(1) If $f'(z) = 0$ for all $z \in \Omega$, then $f$ is a constant function on $\Omega$.
(2) If $|f| = const$, then $f = const$ in $\Omega$.



Let $f$ be a function which is continuous throughout a domain $D$ and suppose that there is an analytic function $F$ such that $F'(z)=f(z)$ for all $z \in D$. Then

$$\int_\gamma f(z)dz = F(z_1)-F(z_0)$$

for any curve $\gamma$ in $D$ with endpoints $z_0$ and $z_1$.（这里我的要积分的函数是continuous的然后F要是analytic的）

definition of contour which is closed and simple and smooth(that is to say it is differentiable)

The Logarithm Function and Branches
The objective is to construct an inverse function to the exponential

A function of two real variables which satisfies Laplace’s equation and
has continuous partial derivatives of the first and second order is called a harmonic function

在complex plane上面没有义differential equation，所以不能直接求解而是通过求导的方式来进行计算

path->coutour->Integral->parameterization does not matter（(因为积分是和路径的参数化无关的(let $\gamma_j$:[$a_j$,$b_j$] $\to$ $\gamma^{*}$ j=1,2 be two paths,parametrising $\gamma^{*}$)
其实这里就是说，我们积分是和路径的参数化无关的,只和起点和终点有关）->fundamental of calculas->antiderivative theorem(还没看proof)->cauchy theorem（）->keyhole lemma->cauchy integral formula（就是用coutour里面的值来描述积分，也可以用积分来描述里面的值）->cauchy integral formula for derivatives（可以证明infinitely differentiable因为每一个differivitive都有值）->morera's theorem(反过来的cauchy therorem，是说如果任意一个三角形积分都是0，那么这个函数就是holomorphic的)->cauchy's inequality（就是我们要指定在哪一个domain（圆圈）上是bounded的（也就是要定义一个圆点位置和半径），然后再说这个函数的一个值的module小于一个k!*M/r^n）->liouville's theorem(entire 很重要也要holomorphic)->fundamental theorem of algebra->cauchy's inequality for the laurent series->classification of singularities->cauchy's residue theorem-> residue theorem->

Bounded是sup|f(z)|<=M

Remember that Arg z is not continuous and so has no derivative at any point on the negative
real axis. So we consider the domain of the principal logarithm to be the whole complex plane
with the negative real axis extracted (including the zero). In other words, this function is
defined on the complex plane with a cut along the negative semi-axis.（也就是我不continous就一定不differentiable）所以我们取的定义域是去掉负半轴的整个复平面。


本质上来讲，由于这个argument function是多值的，所以我们要给他一个定义域，然后我们才能定义一个单值的函数。

当我们定义log的时候一定要说明他的定义域，也就是他的argument function的定义域。
specifically, we define the principal branch of the logarithm by

$$L(z) = \ln|z| + i\arg(z)$$
$(-pi,pi]$
然后我们定义differentiablity的时候，由于这个derivative on negative real axis是不连续的，所以我们要给他一个定义域，然后我们才能定义一个单值的函数。也就是$\pi到-\pi$

we define the principal exponent by g

**Theorem** (Antiderivative Theorem). Let $\Omega$ be a convex domain(i.e. a domain in which any two points can be joined by a line segment) and let $f$ be continuous on $\Omega$, and that

$$\int_\gamma f(z)dz = 0 \tag{5.1}$$

for any triangular contour $\gamma$ such that $\gamma^* \subset \Omega$. Then for any point $a \in \Omega$ the function

$$F(z) = \int_{[a,z]} f(w)dw$$

is a primitive of $f$ on $\Omega$.

consider now a function f which is continuous on some domain $\omega$. We have seen in Theorem 5.8 that if $f$ has an antiderivative then the integral along any contour $\gamma \subset \omega$ is 0.

Question: what conditions should we impose on $f$ and/or $\omega$ to ensure that the integral is zero for any contour $\gamma \subset \omega$?

其实就是antiderivative定理说明如果现在这么一个函数是连续的而且对于任何一个在domain里面的三角形积分都是0，那么这个函数就有antiderivative。那么我们就会问一个问题说，那么什么时候我才会integral是0呢？

然后发现如果这个函数是holomorphic的，那么这个integral就是0。

and 

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

for any point $a$ inside $\gamma$(the condition is that the point a is inside the contour $\gamma$).   

notion:(we need to satisfy the condition that the the function in the chosen domain is holomorphic, for example, the function $f(z) = \frac{1}{z}$ is not holomorphic on the domain that contains the origin, so we cannot use the Cauchy Integral Formula on the origin, also $f(z) = \frac{cosz}{1+z^2}$ is not holomorphic on the domain that contains the point $z = i$(disk D(2i,0)), so if we cannot use the Cauchy Integral Formula in that domain, we need to find other methods to solve the problem,like trying to deal with the function into another form that can make the function to be holomorphic on the domain)
他的点一定要在interior里面

他这个证明的关键在于对于一个确切的点，他的导数一定是bounded的

也可以理解为在这么一个contour里面的点的值乘以2pi i 可以得到这么一个积分

反过来积分也可以找值来表达


**Cauchy Integral Formula for Derivatives**: Let $f$ be holomorphic on a domain $\Omega$(simply connected) and let $\gamma$ be a closed contour in $\Omega$. Then

$$f^{(n)}(a) = \frac{n!}{2 \pi i} \int_\gamma \frac{f(z)}{(z-a)^{n+1}}dz$$

for any point $a$ inside $\gamma$.  (be careful with the power of the denominator to have power $n+1$)


Morera's Theorem:
Let $f$ be continuous on a domain $\Omega$ and that

$$\int_\gamma f(z)dz = 0$$

for any triangular contour $\gamma \subset \Omega$. Then $f$ is holomorphic on $\Omega$.

ok之前第一个antiderivative定理是说如果一个函数是连续的，然后对于任何一个在domain里面的三角形积分都是0，那么这个函数就有antiderivative, 然后我们又知道了如果一个函数是anlytic的那么，在一个domain上任意一个contour的积分都是0，那么反过来，如果一个函数连续而且在domain上任意一个contour的积分都是0，那么这个函数就是analytic的。（其实就是我有premitive就可以求导然后在complex function中就就可以一直holomorphic） 其实这里产生了一个问题对于一个complex function它可以通过换元得到结果，但是这个function不一定是holomorphic不就很奇怪吗


**Cauchy's Estimate**: Let $f$ be holomorphic on a domain $\Omega$ and let $D(a,r)$ be a disk(it can have boudary) in $\Omega$. Then

$$|f^{(n)}(a)| \leq \frac{n!M}{r^n}$$

for any $M > 0$ such that $|f(z)| \leq M$ for all $z \in D(a,r)$.

这里是说，我们定义一个f是holomorphic的，然后假设一个包含边界的圆同样属于这么一个domain（open connected set），然后我们说这个函数在这么一个圆上的值的module小于等于一个M，然后我们就可以得到他的n阶导数的值的module小于等于一个k!*M/r^n。

**Liouville's Theorem**: Let $f$ be entire and bounded(i.e. $|f(z)| \leq M$ for all $z \in \mathbb{C}$). Then $f$ is constant.

Let $p(z)$ be a non-constant polynomial. Then $p(z)$ has a root in $\mathbb{C}$.

any polynomial of degree $n$ has $n$ roots in $\mathbb{C}$
感觉现在modulus有点问题

5.24 Let $p(z)$ be a non-constant polynomial with complex coefficents Then there exists a complex number $a$ such that $p(a)=0$

**Uniform Convergence**:
we now consider the convergence of a sequence of functions $f_n(z)$ to a function $f(z)$ on a domain $\Omega$.

we say this sequence converges pointwise to another function $f$ on $\Omega$ if for every $\epsilon > 0$, there exists an integer $N$ such that

$$|f_n(z) - f(z)| < \epsilon$$

for all $z \in \Omega$ and for all $n \geq N$.

we say this sequence converges uniformly to another funtion $f$ if sup$|f_n(z) - f(z)| \to 0$ as $n \to \infty$ uniformly on $\Omega$.

the uniformity emphasizes that the same $N$ works for all $z \in \Omega$.

the uniform convergence can be rephrased by saying the sequence a_n=sup|f_n(z)-f(z)| converges to 0 as $n \to \infty$（where z is in $\Omega$
uniform convergence is implies pointwise convergence.

为啥这么定义

也就是我要定义两个东西第一个逼近的函数，第二个是找到一个domain，在这个domain上，这个函数和逼近的函数之间的差值小于一个很小的数。也就是pointwise convergence。这个N取决于（z and $\epsilon$）

uniform convergence是说，这个N只取决于$\epsilon$，和z无关。因为我这里描述的是sup($z \in \Omega$)||f_n(z)-f(z)||,每次都是取得最大的那么一个值

就相当于我的uniform convergence要保证对于 $\forall z \in \Omega$, 存在一个N，使得都converge，而不是对于特定的z我存在一个不同的N。
(感觉就是我的uniform convergence是对于所有的z，所以���想让我这个逼近的函数尽可能完美，所以考虑最差的情况，就是sup然后如果等于0说明对于任一点都收敛的很好)
uniform convergence of series: we say that the series $\sum_{n=1}^{\infty} f_n(z)$ converges uniformly on $\Omega$ if the sequence of partial sums $s_n(z) = \sum_{k=1}^{n} f_k(z)$ converges uniformly on $\Omega$.(这是一个definition就是描述说我们怎么定义一个series的uniform convergence)

这样的话我们可以定义uniform convergence sequences的计算 limit和integration因为每一个N都是一样的。

corollary 5.18还没看 antiderivitive 没看懂


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
我必须要让f在$D(z_0,r)$上analytic，然后我才能用泰勒定理，而且选的点$z_0$必须在$D(z_0,r)$上。（他要保证里面每一个点的series都converge e为了使用泰勒级数展开，我们需要确保以下条件：

1. 函数 $f(z)$ 在圆域 $D(z_0,r)$ 内解析（analytic）
2. 展开中心点 $z_0$ 必须位于该圆域内
3. 对于圆域内的每一点，级数都必须收敛

例如，对于函数 $\frac{1}{3+z^2}$


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
$\frac{1}{\sin(\frac{\pi}{z})}$是一个有趣的函数 他除了z=0以外存在��singular point 都是isolated singularity但是对于z=0他不是isolated singularity？？

**Definition 6.6**: let $a$ be an isolated singularity of $f$. The residue of $f$ at $a$, denoted by $\operatorname{Res}(f,a)$, is the coefficient $c_{-1}$ in the Laurent expansion of $f$ at $a$:

$$f(z) = \sum_{n=-\infty}^{\infty} c_n (z-a)^n$$    
notes说这个很特么有用，接着往下看吧 </br>‘


也就是我们用cauchy's residue theorem来计算integral（如果integral function里面有singularity），同时这个residue也可以被expansion过后的a_(-1)表示，记住integral的值是这residue乘上2pi i,这是一种计算方法，还有一种就是直接用cauchy's integral formulae 来计算，然后记住如果是differentiate那么我们要除以一个阶乘

**Cauchy's Residue Theorem**: let $f$ be analytic on an annlus $A(a,r_1,r_2)$ except for finitely many isolated singularities $a_1,a_2,...,a_N$ at $a$. Let $\gamma$ be a closed contour in $A(a,r_1,r_2)$ that contains $a$ in its interior and suppose that $\gamma$ is positively oriented. Then

$$\int_\gamma f(z)dz = 2\pi i \sum_{k=1}^{N} \operatorname{Res}(f,a_k)$$

(注意这里一定要是isolated singularities)

这里的contour必须是一个positively oriented的contour，并且包含$a_k$，而且$a_k$是contour内部唯一的singularity。


classification of singularities:

There are 3 types of singularities:

If the negative part of the expansion of $f$ has only finitely many terms, $sum_{n=-\infty}^{-1} c_n (z-a)^n$, then $a$ is a pole.

If the negative part of the expansion of $f$ has infinitely many terms, then $a$ is an essential singularity.

If the negative part of the expansion of $f$ has only finitely many terms and the coefficient of $(z-a)^{-1}$ is 0, then $a$ is a removable singularity.（就是周围可以analytic但是这个点取不到，然后我们可以定义一个点）

And if we defnie $f(z_0)=a_0$,then the function becomes analytic in a neighbourhood of z_0

Suppose that $f \in H(D'(z_0,r))$ is bounded. Then $f$ has a removeable singularity at z_0

Let $f \in H(D'(z_0,r))$, the function f has a pole of order m at z_0 if and only if it can be represented in the form
 
$f(z)=h(z)/(z-z_0)^m$ where $h(z)$ is analytic and nonzero at z_0. 这个就相当于ok我现在给你乘出来，然后如果holomorphic了,那么就说明他的次数最多也就这样了(问题如果出现说$h(z)=0$怎么处理)

现在考虑上下限是无穷的情况
(考虑R->无穷)
那么基本思路是构造一个closed contour

就是构造一个半圆和一条直线，然后利用Cauchy's integral formula

**Lemma 6.10:** Suppose that $f$ is continuous on the semi-circle $\gamma$, and suppose that $\max|f(z)| \leq \frac{C}{R^k}$ for all $R \geq R_0 > 0$ with some $k > 1$ 
(这里能调k是因为我们希望他最后能收敛到0，所以k越大收敛越快). Then 
$$\int_\gamma f(z)\,dz = 0, \quad R \to \infty$$
and 
$$\lim_{R \to \infty} \int_\gamma f(z)\,dz = \int_{-\infty}^{\infty} f(x)\,dx$$

这个感觉可以自己调k，其实就是这个standard integral bound有很多可能可以尝试调系数

**Jordan's Lemma**:
Sometimes it is necessary to use a deeper argument to show that the integral round the semi-circle approaches 0 as $R \to \infty$.

Let $f$ be a function continuous in the domain $\Omega={ z \in \mathbb{C}:Im z \geq 0 \text{ or }, |z|>R_0 }$ with some $R_0 \geq 0$ and suppose that $M(R)$ is the maximum value of $|f(z)|$ on the semi-circle $r=R$. Then

$$\int_\gamma e^{iaz}f(z)\,dz \to 0 \text{ as } R \to \infty$$
where $\gamma_R = \{z = Re^{i\theta} \mid 0 \leq \theta \leq \pi\}$

Suppose that $f \in H(D'(z_0,R))$ is bounded, Then $f$ has removable singularity at $z_0$


analysis今年的notes
去年的notes
做题
mobius
展开



半期总结，看时间对我影响太大，以及直接放弃一种方法，以及注意principal part是对于这个singularity来构建的