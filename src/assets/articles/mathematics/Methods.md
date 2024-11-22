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
