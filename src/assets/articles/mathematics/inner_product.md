# Proving Cauchy-Schwarz Inequality

## Start: Prove Cauchy-Schwarz Inequality

$\sum_{i=1}^n x_i^2 \cdot \sum_{i=1}^n y_i^2 \geq (\sum_{i=1}^n x_iy_i)^2$

My idea is to use notation $\vec{x} \cdot \vec{y}$ and $|\vec{x}|, |\vec{y}|$ for vectors $\vec{x} = \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}$

So: $\sum_{i=1}^n a_ib_i \geq \sqrt{\sum_{i=1}^n a_i^2} \cdot \sqrt{\sum_{i=1}^n b_i^2}$

Therefore: $(\sum_{i=1}^n a_ib_i)^2 \geq \sum_{i=1}^n a_i^2 \cdot \sum_{i=1}^n b_i^2$

But this is "totally wrong" as we need Cauchy-Schwarz inequality to be proved first as we use Cauchy-Schwarz to prove inner product.

Logic chain: Cauchy-Schwarz ⇒ Inner product

So we now need to figure out why $(\sum_{i=1}^n a_ib_i)^2 \geq \sum_{i=1}^n a_i^2 \cdot \sum_{i=1}^n b_i^2$ is true.

## Vector Approach

What we need to prove is $|u \cdot v| \leq |u||v|$

And we think about what comes next:
1) What can we do ⇒ We may be able to find the relation with $u$ and $v$ ⇒ So consider $\vec{u} + t\vec{v}$
,and consider the quadratic function:
$f(t) = (\vec{u} + t\vec{v}) \cdot (\vec{u} + t\vec{v})$
$= |\vec{u}|^2 + 2t(\vec{u} \cdot \vec{v}) + t^2|\vec{v}|^2$

This quadratic function $f(t)$ represents the inner product of the vector with itself, which must be non-negative for all real $t$.

So $f(t)$ must be $\geq 0$ ⇒ $\Delta(f(t)) \leq 0$

## Quadratic Inequality

Consider the quadratic inequality:

$4(u \cdot \vec{v})^2 - 4|\vec{u}|^2|\vec{v}|^2 \leq 0$

This implies:

$(u \cdot \vec{v})^2 \leq |\vec{u}|^2|\vec{v}|^2$

Therefore:

$|u \cdot \vec{v}| \leq |\vec{u}||\vec{v}|$

This is the Cauchy-Schwarz inequality in its vector form, which is equivalent to our original inequality for sequences.

## Note on Approach
But why we consider this quadratic? I search online and it takes me to the world of inner product.

The quadratic approach provides an elegant proof of the Cauchy-Schwarz inequality by connecting the geometric interpretation of inner products with algebraic properties of quadratic functions. This connection is fundamental in understanding both inner product spaces and inequalities in mathematical analysis.

[Note: This appears to be exploring the connection between the Cauchy-Schwarz inequality and inner product spaces]