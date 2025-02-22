# algebra review


Field->F-vector space->subspace->The intersection of two subspaces is a subspace->sum of U and W is a subspace->linear combination->linearly independent->span->spanning set->basis->steinitz exchange lemma->We will see in the Jordan Normal Form section how useful this trick is.->(Corollary 2.10. Suppose V is an F-vector space with a basis of size n. Then
1. Every basis of V has size n.
2. Any linearly independent set of size n is a basis.
3. Every spanning set of size n is a basis.
4. Every finite spanning set contains a basis.
5. Every linearly independent subset of V can be extended to basis)->dimension->dim(proper subspace)< dim(the space) ->Linear Maps(isomorphism, endomorphism, automorphism)->T-invariant(是用来描述subspace的)-> restriction->kernal and image->(linear map)$T:V \to W$ be linear.Then T is injective<=>KerT={0} and T is surjective<=> ImT=W
If T is injective and S is a subspace of V then T(S) is a linearly independent set in W-> T is surjective and S spans V, then T(S) spans W->linear maps and matrices（there is a bijection between linear maps and matrices）->rank nullity Theorem->(internal)direct sum(complementary subspaces)->If V=U+W(direct sum here) if and only if every v can be written uniquely as u+w()








## bilinear and Hermitian forms

Let $V$ and $W$ be two $F$-vector spaces. A bilinear form on $V$ and $W$ is a map $B: V \times W \to F$ such that for all $v \in V$ and $w \in W$, $B(v,w)$ is linear in $v$ and $w$. 
(也就是 $B(v,-):W \to F$ 和 $B(-,w):V \to F$ 都是线性的)
个人感觉是控制其中一个变量改变，另一个变量保持不变，然后看这个变化是否是线性的。


matrix representation of bilinear forms


**Definition 1.3.** Let $\{v_1,\ldots,v_n\}$ be a basis for $V$, $\{w_1,\ldots,w_m\}$ be a basis for $W$, and $\phi: V \times W \to F$. Then the matrix representing $\phi$ is defined to be 

Bilinear form: 可以被expressed to be a matrix

When coming to bilinear forms, the matrices representing transformation of basis acts differently with linear maps.
Focus on bilinear $\phi: V \times V \to F$

Bilinear form其实就是一个function把两个vector space Cartesian product出来的一个值

**Proposition 1.5.** Let $\phi: V \times V \to F$ be a bilinear form and let $A$ be its matrix representation with respect to a basis $\{v_1,\ldots,v_n\}$. If we change to a new basis using an invertible transformation matrix $P$, then the matrix representation $B$ of $\phi$ with respect to the new basis is given by:

$B = P^{\top}AP$

The difference with the transformation laws of matrices is this time we are taking transposes not inverses.

Two square matrices $A,B$ are congruent if there exists some invertible matrix $P$ such that $B = P^{\top}AP$.

A bilinear form $\phi: V \times V \to F$ is degenerate if the left and right kernels are trivial.

$\text{Rank}(P^{\top}AP) = \text{Rank}(A)$ for any invertible matrix $P$ (prove?)

Let $\phi_L: V \to V^*$ be defined by $\phi_L(v)(w) = \phi(v,w)$

Let $\phi_R: V \to V^*$ be defined by $\phi_R(v)(w) = \phi(w,v)$

The matrix representation of $\phi_L$ with respect to the same basis and the corresponding dual basis for $V^*$ is $A^T$.
The matrix representation of $\phi_R$ with respect to the same basis and the corresponding dual basis for $V^*$ is $A$.

**Theorem:** $\phi$ is non-degenerate if and only if $A$ is invertible (equivalently, $A$ is full rank).

### Symmetric and Quadratic Forms

A symmetric bilinear form is a specific type of bilinear form where $\phi(v,w) = \phi(w,v)$ for all $v,w \in V$.

For example, if $\phi(v,w) = v^T w$, then $\phi(w,v) = w^T v = v^T w = \phi(v,w)$.

**Proposition:** If $S$ is the matrix representation of $\phi$ and $\phi$ is symmetric, then $S = S^T$.

Definition 2.5 Let $\phi: V \times V \to F$ be a symmetric bilinear form. The quadratic form associated with $\phi$ is the map $q: V \to F$ defined by $q(v) = \phi(v,v)$ for all $v \in V$.

q is not a linear map it is quadratic
e.g., $q(x) = x^{\top}Sx = ax^2 + 2bxy + cy^2$ (其实无非就是 $q(v) = \phi(v,v)$)

**Polarisation Identity:** Suppose $\text{char}(F) \neq 2$, for any quadratic form $q$, there exists a unique symmetric bilinear form $\phi$ such that $q(v) = \phi(v,v)$, where:

$\phi(u,v) = \frac{1}{2}(q(u+v) - q(u) - q(v))$

Diagonalisation of Symmetric Bilinear Forms

Let $V$ be a vector space over $F$ with a symmetric bilinear form $\phi$, we call two vectors $v,w \in V$ orthogonal if $\phi(v,w) = 0$. This is written as $v \perp w$. If $S \subset V$ then the orthogonal complement of $S$ is $S^{\perp} = \{v \in V \mid \phi(v,s) = 0 \text{ for all } s \in S\}$

For any subspace $S \subseteq V$, $S^{\perp}$ is a subspace of $V$

A basis $B = \{v_1,\ldots,v_n\}$ for $V$ is called orthogonal if $\phi(v_i,v_j)=0$ for all $1 \leq i < j \leq n$. Hence, $B$ is an orthogonal basis if and only if $\phi$ is represented by a diagonal matrix with respect to $B$.

Let $V$ be a finite-dimensional vector space over $F$ with a symmetric bilinear form. Then there exists an orthogonal basis for $V$ with respect to $\phi$.

Let $A$ be a symmetric matrix where char $F \neq 2$. then $A$ is congruent to a diagonal matrix

A double operation means performing a row operation followed by the corresponding column operation

why we can do a sequence of double operations to transform $A$ to a diagonal matrix?
也就是我们先perform一个row operation，然后perform一个对应的column operation，然后我们就可以把$A$变成一个对角矩阵。

Let $\phi$ be a symmetric bilinear form over a complex vector space.Then there exists a basis $v_1,....,v_n$ for $\mathbb{V}$ such that $\phi$ is represented by a diagonal matrix with respect to $B$.

Every symmetric matrix is congruent to a diagonal matrix. （这个东西就相当于看这么一个bilinear map的rank，也就是到底有多少个independent directions where the bilinear form is "active" or "non-degenerate"这个r is the number of non-zero eigenvalues of the matrix representing the bilinear form）

orthogonal vectors: $\phi(v,w) = 0$

orthogonal basis: $\phi(v_i,v_j) = 0$ for all $1 \leq i < j \leq n$ 


现在要证明uniqueness

Sylvester's law of inertia
Let $\phi$ be a symmetric bilinear form over a real finite dimensional vector space $V$. Then exists unique integers $p,q>=0$ such that $\phi$ is represented by the diagonal matrix diag$(1,\ldots,1,-1,\ldots,-1)$ with respect to some orthogonal basis for $V$. Here $p+q = \text{rank}(\phi)$

# Hermitian Forms

a sesquilinear form is a generalization of a bilinear form where the field is extended to the complex field and the multiplication is modified to be conjugate linear in the second variable.

其实可以理解为，在bilinear form的基础上，我们把第二个变量乘以一个复数，然后我们把这个复数取共轭，然后再乘以第一个变量。

A sesquilinear form on $V \times V$ is Hermitian if $\phi(v,w) = \overline{\phi(w,v)}$ for all $v,w \in V$.

sesquilinear 是定义在vector space上面的 这是一个function，然后hermitian是其中一个特殊的作用在vector space上面

If $V$ is $C^{n}$ then every Hermitian form may be represented as $\phi(v,w)=v^{T}Aw$ for some $A \in M_{n}(C)$

Let $V$ be a complex vector space and let $\mathcal{B} = \{v_1,\ldots,v_n\}$ be a basis for $V$. and $C=\{w_1,\ldots,w_n\}$ be the corresponding dual basis for $V^{*}$. with associated matrix representation $A$. If $\phi$ is a Hermitian form on $V$ with associated matrix $\mathcal{B}$ with respect to basis $\mathcal{B}$, and $C$ with respect to dual basis $C$, then $A = P^{T}AP$ for some invertible matrix $P$.    
（问题为什么conjugate挺好，为什么考虑conjugate,考虑基础的算式(或者考虑一个mapping)）
其实基于这个我们发现operation必须变成conjugate的

Inner Product Spaces(In linear algebra one is often intereted in the canonical forms of a linear transformation .Given a particularly nice basis for the vector space in which one is working, one can often find a canonical form for the linear transformation that is particularly easy to understand and work with.(spectral theorem))
Hilbert Space(A Hilbert space is a vector space with an inner product that is complete with respect to the norm defined by the inner product. Hilbert spaces are fundamental to many areas of mathematics and physics, including quantum mechanics and partial differential equations.)

inner product on $V$ on V is a mapping that takes two vectors and returns a scalar and satisfies the following properties:

linear in the first variable and the second variable

$\langle x,y \rangle = {\langle y,x \rangle}$

positive definiteness $\langle x,x \rangle \geq 0$ and $\langle x,x \rangle = 0$ if and only if $x = 0$

consider the inner product on $C^n$
we only need to change the definition on $\langle x,y \rangle = \overline{\langle y,x \rangle}$

A finite dimensional real inner product space is called a Euclidean vector space.
A complex inner product space is a unitary space or a pre-Hilbert space. A finite dimensional complex inner product space is a finite dimensional Hilbert space.

LET $V$ be an inner product space. The map $T: V \to V^{*}$ defined by $T(v) = \langle v,w \rangle$ for all $w \in V$ defines an isomorphism from $V$ to $V^{*}$. this is to say T(v)(w) = $\langle v,w \rangle$ = V^{*}($w$)(injectivity+dim相等=isomorphism) keep the structure

In a real or complex inner product space the length or inner 

we say v,w are orthogonal if $\langle v,w \rangle = 0$

orthogonal basis: $\langle v_i,v_j \rangle = 0$ for all $1 \leq i < j \leq n$ and orthonormal basis(就是单位长度)
（也就是我们每个向量可以先由单位长度的向量表示）
Every finite dimensional inner product space has an orthonormal basis.

we define a set orthogonal to T,that is to say $T^{\perp} = \{v \in V \mid \langle v,w \rangle = 0 \text{ for all } w \in T\}$(T is a subset of V)

proposition $V=T+T^{\perp}$

orthogonal projection: $V \to T$ with $V \to \sum_{i=1}^{n} \langle v,t_i \rangle t_i$

Gram-Schmidt process:

let $v_1,v_2,...,v_n$ be a basis for $V$

$u_1 = v_1$

$u_2 = v_2 - \frac{\langle v_2,u_1 \rangle}{\langle u_1,u_1 \rangle}u_1$

$u_3 = v_3 - \frac{\langle v_3,u_1 \rangle}{\langle u_1,u_1 \rangle}u_1 - \frac{\langle v_3,u_2 \rangle}{\langle u_2,u_2 \rangle}u_2$

就是减去projection在其他向量上的投影就会只剩orthogonal的部分

Adjoints and the spectral theorem

we define the adjoint of a linear operator $T:V \to V$ to be the unique linear operator $T^{*}:V \to V$ such that $\langle Tx,y \rangle = \langle x,T^{*}y \rangle$ for all $x,y \in V$

and $[T^{*}]_{\mathcal{B}} = (\overline{[T]_{\mathcal{B}}})^{\top}$

也就是adjoint的矩阵是原矩阵的共轭矩阵的转置

An endomorphism $T:V \to V$ is self-adjoint if $T^{*} = T$
and this is just the Hermitian form

Let $T:V \to V$ be a self-adjoint operator on a finite-dimensional complex inner product space $V$. Then every eigenvalue of $T$ is real. and if $\lambda$ and $\mu$ are distinct eigenvalues of $T$ with corresponding eigenvectors $v$ and $w$, then $v$ and $w$ are orthogonal.(v,w)=0


(spectral theorem for self-adjoint endomorphisms) Let V be a finite-dimensional inner product space over $F$ and let $T:V \to V$ be a self-adjoint operator on $V$. Then there exists an orthonormal basis $\mathcal{B}$ for $V$ consisting of eigenvectors of $T$. Moreover, the eigenvalues of $T$ corresponding to $\mathcal{B}$ are all real.

An orthogonal matrix is an $n \times n$ matrix $\mathcal{O}$ with real entries such that $\mathcal{O}^{T}\mathcal{O} = I$
an orthogonal matrix is a square matrix such that P^T P = I

Let $A$ be a real symmetric matrix.Then there exists an $n \times n$ orthogonal matrix $P$ such that $P^{T}AP$ = $P^{-1}AP$ is a diagonal matrix.

A unitary matrix is an $n \times n$ matrix $U$ with complex entries such that $\overline{U}^{T}U = I$

$\overline{P}^{T} = \overline{P^{-1}}$ is for complex matrix

Let $T:V \to V$ be a self-adjoint operator on an inner product space, then $m_T(x)$ and consequently $\chi_T(x)$ factors into linear factors:

$m_T(x)=(x-\lambda_1)(x-\lambda_2)\cdots(x-\lambda_n)$

where $\lambda_1,\lambda_2,\dots,\lambda_n$ are the eigenvalues of $T$
定理：设 $T:V \to V$ 是内积空间上的自伯算子（self-adjoint operator），则：

1. $T$ 的极小多项式 $m_T(x)$ 可以分解为线性因子的乘积
2. $T$ 的特征多项式 $\chi_T(x)$ 也可以分解为线性因子的乘积

即：$m_T(x) = (x-\lambda_1)(x-\lambda_2)\cdots(x-\lambda_k)$
其中 $\lambda_1, \lambda_2, \dots, \lambda_k$ 是 $T$ 的特征值（全部为实数）。

we now wish to explore the structure of the matrices associated to these self-adjoint linear maps, and we will work towards a proof of the spectral theorem for self-adjoint endomorphisms.

如果一个矩阵是endomorphism，and $T$ 的特征多项式 $\chi_T(x)$ 也可以分解为线性因子的乘积, 就存在一个orthonormal basis of $V$ such that T is represented by an upper triangular matrix.

Let $V$ be a real inner product space and let $T \in \mathcal{End}(V)$. Then the following are equivalent: i)T is self-adjoint,ii)there exists an orthonormal basis for $V$ such that $T$ is represented by a diagonal matrix.iii)$V$ has an orthonormal basis consisting of eigenvectors of $T$.

T is called normal if $TT^{*} = T^{*}T$ ie. T commutes with its adjoint.

A lot of important calasses of matrices are normal but not self-adjoint. such as orthogonal and unitary matrices

T is normal if and only if $\|Tv\| = \|T^{*}v\|$ for all $v \in V$

Schur's theorem: Let $T \in \mathcal{End}(V)$ be a normal operator on a finite-dimensional complex inner product space $V$. Then there exists an orthonormal basis such that the matrix representing the endomorphism is upper triangular.

## Finally,we observe that if a matrix is symmetric or hermitian or orthogonal or unitary,then the matrix is diagonalizable.

