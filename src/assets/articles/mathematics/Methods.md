# methods review


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
