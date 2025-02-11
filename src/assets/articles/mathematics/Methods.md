# methods review


chapter 1:
unit normal vector->surface integral->flux integral->intepretation of the flux integral(流入就是flux<0，流出就是flux>0
1. 闭合曲面的定义
闭合曲面是指将空间分成两个部分的表面，即：
内部（interior）：一个有限的封闭区域。
外部（exterior）：延伸到无穷远的空间。
关键点：从内部到外部必须穿过这个表面，不能绕过去。例如：
球面（如气泡的表面）。
立方体的表面（如一个封闭的盒子）。
任何围成一个封闭体积的三维表面。
2. 闭合曲面的单位法向量（unit normal vector）
对于闭合曲面，我们约定单位法向量始终指向外部，即外法向量（outward-pointing unit normal）。
这样一来，通量的正负可以表示流体是流出还是流入这个封闭区域。3.以及计算通量时，必须指定表面的单位法向量（unit normal vector）。
一般来说，单位法向量并不唯一，可以选择其正负方向。
对于某些特殊的表面，我们通常约定一个特定的方向来定义通量。)->divergence theorem(在向量场的微积分中，我们希望找到衡量向量场在某个点变化的方式。散度的核心思想是通过封闭曲面上的通量来衡量一个向量场在该区域的**源（source）或汇（sink）**特性。那么这个地方我们通过计算当一个小球的体积一直减小，然后通过计算通量来衡量这个向量场在该区域divergence，对于定义中虽然使用了球 S_\epsilonS ϵ，但实际上任何封闭曲面（只要其收缩到该点）都会得到相同的散度值。这说明散度只与点处的局部性质有关，而不依赖于选取的具体封闭曲面。divergence的推导和证明)->divergence theorem((和fundamental theorem of calculus 很像还没看证明) divF 可以理解为变化率, divF的整合和flux 是一样的（把区间端点变成封闭的一个图形）)-> line integral（感觉没啥主要是可以有两种方法，第一种是parametrization，第二种是分为dx和dy然后来讨论（然后我们讨论的parametrization不影响，但是我们的path的选取会影响））-->现在考虑什么情况可能不影响(path independent) -->考察curl(环量刻画向量场沿封闭曲线的旋转趋势。
旋度刻画向量场在每个点的局部旋转情况，是一个向量场。取一个小面积然后和convergence很像就是take limit)（然后我们介绍了一个方法可以让这个旋度的计算更为简单，但是为什么可以这么用curl？）

1. 循环与旋度：含义和解释
在这一部分，循环和旋度的概念得到了进一步的解释，重点讨论了它们的物理意义和如何从几何和动态的角度理解这两个概念。

循环（Circulation）：
循环度量了一个向量场沿着封闭路径推动粒子的趋势。如果你想象一个小粒子被困在一个封闭曲线上，并受到向量场的作用，循环就表示向量场如何“推动”粒子沿着这个闭合曲线运动。如果循环不为零，意味着向量场在某种程度上使粒子围绕闭合曲线运动。因此，循环给了我们一些关于粒子沿闭合曲线的轨道运动的理解。

旋度（Curl）：
一个向量场在某一点的旋度是一个向量，具有特定的方向和大小：

方向：旋度向量指向的是该点周围旋转最强的轴线，这个方向遵循右手定则。
大小：旋度向量的大小告诉我们该点在该方向上的旋转强度。
要直观理解旋度，可以通过想象一个小的桨轮。桨轮的轴线指向旋度向量的方向。如果桨轮开始旋转，就表示该点的旋度不为零，意味着该点的向量场存在旋转运动。旋度不为零意味着任何放置在该点的小物体（如桨轮）会开始旋转。

2. 旋度的示例：
示例 1：如果向量场 FF 是常量（例如 F = \mathbf{c}F=c，常向量），那么旋度在任何地方都是零，这直观上是因为常向量场没有旋转效应——它不会让桨轮旋转。
示例 2：对于向量场 F(x, y, z) = -y\hat{i} + x\hat{j}F(x,y,z)=−y 
i
^
 +x 
j
^
​
 ，旋度是常数并指向 -k−k 方向。这意味着该向量场绕着 z 轴旋转，如果把桨轮放置在水中，它只有当轴线部分指向 kk 方向时才会旋转。
示例 3：对于向量场 F(x, y, z) = -(y + 1)\hat{i}F(x,y,z)=−(y+1) 
i
^
 ，旋度是 \hat{k} 
k
^
 ，尽管这个场的流动方向是单一的（沿着 xx 轴），但桨轮仍然会旋转，因为一侧的流动比另一侧强，这会导致旋转。因此，尽管向量场本身没有“旋转”，它对桨轮的作用却是旋转的。
3. 无旋向量场与路径独立的线积分：
一个无旋向量场是指它的旋度在所有点上都是零。这意味着该向量场在任何点上都没有旋转运动。

例如，常向量场（如 F = \mathbf{c}F=c）是无旋的，因为在任何地方都没有旋转。
向量场 F(x, y, z) = x\hat{i} + y\hat{j}F(x,y,z)=x 
i
^
 +y 
j
^
​
  也是无旋的，因为它的旋度为零。
当一个向量场的旋度在每个点上都为零时，它的线积分是路径独立的。这意味着在不同路径之间计算的功不依赖于路径，只依赖于起点和终点。

路径独立与旋度：
如果一个向量场 FF 沿某路径的线积分是路径独立的，那么它的旋度在路径的每个点上都必须为零。这是因为路径独立意味着没有旋转，而零旋度正是没有旋转的标志。
4. 关于路径独立性和旋度的引理：
引理表明，如果一个向量场 FF 在某点的旋度不为零，那么这个点的线积分不能是路径独立的。换句话说，如果场存在任何旋转（即旋度不为零），那么沿着不同路径从同一两个点之间的线积分会依赖于路径，因此积分不是路径独立的。

路径独立且旋度为零的例子：
向量场 F(x, y, z) = y\hat{i} + x\hat{j}F(x,y,z)=y 
i
^
 +x 
j
^
​
  的旋度为零，意味着它是无旋的，线积分是路径独立的。通过显式计算旋度可以验证这一点。
旋度不为零且线积分不路径独立的例子：
对于向量场 F(x, y, z) = -y\hat{i} + x\hat{j}F(x,y,z)=−y 
i
^
 +x 
j
^
​
 ，旋度是非零的（为 -2k−2k），这意味着它的线积分不是路径独立的。不同路径上的积分会依赖于路径，因为场具有旋转性质。

 旋度是描述向量场在空间中旋转趋势的量，而路径独立性则是描述向量场在不同路径上积分结果是否一致的性质。

 stokes theorem


我们现在要consider function  
how to optimisation problems over infinite dimensional spaces,consider function as an input and we want to find the “critical function” and similarly we define functional or Gateaux derivative of A(V->R) in the $\epsilon$ direction at a point $f_0$ of V to be  $lim_{t->0}\frac{A(f_0+t*\epsilon)-A(f_0)}{t*\epsilon}$ 
we define the critical point of A as the point where the Gateaux derivative is zero

fundamental theorem of calculus of variations
Suppose that y:[0,1]-> $mathbb{R}$ is a function and we want to find the critical function of the functional $A(y)=\int_0^1(y(t)*(\epsilon(t)))dx$=0 for all smooth functions $\epsilon$ then we have that $A(y)=0$ and $y(t)=0$ for all $t$

Euler-Lagrange equation

$\frac{\partial L}{\partial y} - \frac{d}{dx}(\frac{\partial L}{\partial y'})=0$

Beltrami's identity
$If L(p,q,r) is independent of p and y is a solution of the Euler-Lagrange equation then L(x,y(x),y'(x))-y'(x)*\frac{\partial L}{\partial y'} is a constant$



Let $U \in \mathbb{R}^n$ be an open subset whose boundary $\partial U$ is smooth. We will consider functions $f: \partial U \to \mathbb{R}$ with fixed boundary values; in other words we will fix a function $f_0: \partial U \to \mathbb{R}$ and consider functions $f$ such that $f(x) = f_0(x)$ for $x \in \partial U$.

Perturbations $\epsilon(x)$ satisfy $\epsilon(x) = 0$ for $x \in \partial U$. The Lagrangian $L$ will now depend on $x=(x_1, x_2, ..., x_n)$, on $f(x)$ and on the partial derivatives. That is:

$$A(f) = \int_U L(x,f(x),\nabla f(x))dx_1...dx_n$$

in order to minimize $A(f)$ we need to solve the Euler-Lagrange equation:

$$
\frac{\partial L}{\partial f} - \nabla \cdot \frac{\partial L}{\partial \nabla f} = 0
$$

Important: 
$$\nabla \cdot \frac{\partial L}{\partial \nabla f} = \sum_{i=1}^n \frac{\partial}{\partial x_i}\left(\frac{\partial L}{\partial f_{x_i}}\right)$$
（无非就是现在里面求偏导，然后根据里面的偏导数再求偏导（这个取决于里面的变量））

记住：
$$\frac{\partial \phi}{\partial x} + 2\frac{\partial \phi}{\partial y} = \sin(y)$$
solve the differential equation:
Let's consider the transformation matrix:
$$
\begin{pmatrix}
x \\ y
\end{pmatrix} = 
\begin{pmatrix}
1 & 0 \\
2 & 1
\end{pmatrix}
\begin{pmatrix}
u \\ v
\end{pmatrix}
$$

For a 2×2 matrix, the inverse is given by:
$$
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix}
d & -b \\
-c & a
\end{pmatrix}
$$

Note that in our case, $\det\begin{pmatrix}1 & 0 \\ 2 & 1\end{pmatrix} = 1$, which simplifies the calculation of the inverse.
然后写出逆矩阵：
$$
\begin{pmatrix}
u \\ v
\end{pmatrix} 
= 
\begin{pmatrix}
1 & 0 \\
-2 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y

\end{pmatrix}$$



Therefore:
$$\frac{\partial \phi}{\partial u} = \frac{\partial x}{\partial u}\frac{\partial \phi}{\partial x} + \frac{\partial y}{\partial u}\frac{\partial \phi}{\partial y} = \sin(y) = \sin(2u+v)$$


Nonlinear change of coordinates:
比如如果原先有两个变量，那么我现在也只能有两个变量，比如把我们微分方程的constant其中一个随便选一个，另外一个设为v（另外一个变量）（好像有一些限制）（也就是我们的transformation of variables 过后要保证新坐标能表达原先的旧的坐标（也不完全就是要保证出来的要是一个bijection，但是你得明确说这个transformation过后是在哪个domain里面））其实也就是一直在change of variables(所谓的式子构造的复杂其实有可能是坐标系选择的复杂（但为什么会这样）)


Quasilinear equations:
characteristic vector field
首先考虑一个quasilinear PDE:
$$a(x,y,u)\partial_x u + b(x,y,u)\partial_y u = c(x,y,u)$$
然后我们假设我们已知一个解$u(x,y)$,就是z然后我们求解出这个function过后，把z通过x和y表达就好（x，y，z都会被一个变量表达）
这个东西很像点乘=0，然后我们考虑characteristic curve which is a solution of the following ODE:

$$
\frac{dx}{dt} = a(x,y,u), \frac{dy}{dt} = b(x,y,u), \frac{du}{dt} = c(x,y,u)
$$

然后我们再introduce a surface $S$ which is a graph of a function z=$\phi(x,y)$
就是这个graph不能有vertical 

## Caustics

Let (s,t)->(x(s,t),y(s,t),z(s,t)) be a surface in $\mathbb{R}^3$.The surface is said to have a vertical tangency at (x,y,z) if some linear combination of the vectors

$$
\frac{\partial x}{\partial s}, \frac{\partial y}{\partial s}, \frac{\partial z}{\partial s}
$$
$$
\frac{\partial x}{\partial t}, \frac{\partial y}{\partial t}, \frac{\partial z}{\partial t}
$$
is $\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$.

Take the set of points where the surface has a vertical tangency and project it to the (x,y) plane. The image is called of the surface.

Check remark 9.10 at page 53
caustic有点像光线折射和反射的envelope(an envelope of a plane curve is a curve which is tangent to each member of the family at some point)
we also consider the projection of the surface onto the $(x,y)$ plane and define $\pi(s,t) = (x(s,t),y(s,t))$. A point $(s_0,t_0)$ is called a critical point of $\pi$ if the Jacobian determinant is zero:

$$\det\begin{pmatrix} 
\frac{\partial x}{\partial s} & \frac{\partial y}{\partial s} \\
\frac{\partial x}{\partial t} & \frac{\partial y}{\partial t}
\end{pmatrix} = 0$$

The image under $\pi$ of the set of critical points is called the set $C(\pi)$ of the surface
而且$C(\pi)$ 包含caustic 并不是说$C(\pi)$ 就是caustic，而是说caustic是$C(\pi)$的子集，这是因为 it is possible for the parametrisation of the surface itself to have a singularity so that the vectors $\frac{\partial x}{\partial s}, \frac{\partial y}{\partial s}, \frac{\partial z}{\partial s}$ are linearly dependent at such points.
lemma 9.12 The set $C(\pi)$ of critical values of the projection $\pi$ contains the caustic of the surface.
总感觉整体思路很像把pde变成ode，然后求解ode，然后通过ode的解来反求pde的解


D'Alembert method:
linear second_order hyperbolic equations with constant coefficients


Hyperbolic equations:
The wave equation belongs to the class of hyperbolic second_order linear equations
$\phi(x,t)=C_1(x+t)+C_2(x-t)$
wave equation solution

this is due to $\partial_x^2 -\frac{1}{c^2}\partial_t^2 = 4\partial_{x+}\partial_{x-}$

$$A\partial_t^2 \phi + B\partial_t\partial_x \phi + C\partial_x^2 \phi = D(x,y)$$
Where A,B,C are constant and D is a given function of x and y.
we will find coordinates(s,t) so that the equation becomes A\partial_s\partial_t \phi = D(x,y)

and the transformation is will be $x=s+t,y=-\beta s-\alpha t$


$$A\partial_t^2 \phi + B\partial_t\partial_x \phi + C\partial_x^2 \phi = D(x,y)$$ 

如果B^2-4AC>0，那么这个方程是双曲型(hyperbolic)的，如果B^2-4AC=0，那么这个方程是抛物型(parabolic)的，如果B^2-4AC<0，那么这个方程是椭圆型(eliptic)的。

我们的transformation是hyperbolic的
然后这里a和p是通过求解A，B，C的那个二元一次方程得到的 
