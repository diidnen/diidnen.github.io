Metric Topology and Point-Set Topology Motivation

Metric Space as an Intuitive Framework

metric topology is the morally correct way to motivate point-set topology as well as to generalize normal calculus(metric space 是一种更直觉而且它保留了很多概念，而让这些概念能被更intuitive)

discrete metric space can be thought as graph

因为我们都在metric空间中考虑距离了，那么根据我们convergent的定义其实我们也可以来考虑一下converge

Convergence in Metric Spaces

converge in metric space

Continuity in Metric Spaces

同理我们也可以构造continuity of any function in metric space(this generalization is good因为我们立马就可以考虑其他满足metric space的空间 比如在C中的定义)

然后我们定义sequential continuity(as it is easy to use)

composition of continuous functions is continuous

Homeomorphism

in metric space we do exactly the same thing as isomorphism. We called this as homeomorphism.

Let M and N be metric spaces, A function f:M->N is a homeomorphism if it is a bijection, and both f:M->N and its inverse are continuous.We say M and N are homeomorphic(也可以理解为equivalence relation,我们之所以要定义inverse是continuous因为,inverse in metric or topological spaces (bijection and continuity of a function are not enough so we need the inverse to be continuous))

Homeomorphism and Size Preservation

homeomorphism really do not preserve size, the open interval,(-1,1) is hmomeomorphic to the real line R one such bijection is given by $x \to \tan(\frac{x\pi}{2})$

而且我们要描述距离 那么可以用close来描述 how a function behaves close to certain point p

Product Metric

product metric（$M \times N$)

Convergence in the product metric is by component $(x_n,y_n) \to (x,y) if and only if x_n \to x and y_n to y$

The addition and multiplication maps are continuous maps $R \times R \to R$

r-Neighborhood and Convergence

然后我们定义r neighbourhood来定义convergence.specifically a sequence (x_n) converges to x if for every r-neighbourhood of x, all terms of x_n eventually stay within that r-neighborhood

Epsilon-Delta Definition

然后 we require that the pre-image of every $\epsilon-neighborhood has the property that some \delta-neighborhood exists inside it$ 然后我们定义open 然后我们又回到说open能告诉我们什么 A fumnction $f:M \to N$ of metric spaces is continuous if and only if the pre-image of every open set in N is open in M

Open and Closed Sets

考虑complement

现在证明如果M是一个metric space S is a subset of M. Then the following are equivalent:
The set S is closed in M
The complement M\S is open in M

open其实和closed的定义是完全不同的，open是我们可以找到一个圆，但是closed是我们的极限x也在这个space里面(注意subspace的不同)

比如（[0,1]并(2,3)，然后对于interval([0,1],(2,3)都是open 和closed的，我们证明一个就行，对于[0,1]open，也就是，我们[0，1]可以由 union of open balls in X of raduis 1 about each of their points）

Closed and Complete Sets

closed and complete: complete 一定 closed, closed 不一定 complete,感觉closed很不强，A subset S in M is closed in M if the floowing property holds:let x_1,x_2.... be a sequence of points in S and suppose that x_n converges to x in M. Then $x \in S$ as well（就是必须要保证有converge在M里面（上面例子），然后同时也在s里面）

Boundedness

A metric space M is bounded if there is a constant D such that $d(p,q)\leq D$ for all $p,q \in M$

a discrete space on an infinite set is bounded might be upsetting to you

A metric space is totally bounded if for any $\epsilon >0$,we can cover M with finitely many $\epsilon-neighborhood$
totally bounded implies boundedfor topological spaces it may be easier to consider open sets
to start with A function f:M->N of metric spaces is continuous if and only if te pre-image of every open set in N is open in M(在这个theorem中，我们只描述了open的性质)

definition of topological space: A topological space is a pair (X,T), where X is a set of points, and T is the topology, which consists of several subsets of X, called the open sets of X,called the open sets of X th topology must obey some axioms

discrete space is a topological space in which every set is open(the collection of opensets is defined as the power set of X thsi means that every subset of X is an open set)
we now redefine
we define continuous homeomorphism
and we find that any property defined only in terms of open sets is preserved by homeomorphism
In a general topological space X, we say that S be a subset of X is closed in X if the complement X\S is open in X. If S is a subset of X is any set, the closure of S denoted $\bar{S}$ is defined as the smallest closed set containing S

然后我们从这里可以发现其实open或者closed其实contain同等information，但是我们prefer open
然后对于complete and totally bounded is not working(as (0,1) is isomorphism to R)
and for sequences if we introduced it, this turns out to break a lot of desirable properties, and if we re discussing sequences you should assume that we are working with a metric space

open定义: This means for each point $x \in A$, there exists a rational neighborhood around x that is entirely contained within A


Hausdorff spaces

for topological spaces which cannot be realized as metric spaces cause X={a,b,c} and t_X= ${\emptyset,{a,b,c}}$ this topology is fairly stupid, it cannot tell apart any of the points a,b,c! but any metric space can tell its points apart

A topological space X is Hausdorff if for any two distinct points p and q in X, there exists an open neighborhood U of p and an open neighborhood V of q such that $U \cap V=\emptyset$

In other words, around any two distinct points we should be able to draw disjoint open neighborhoods.

Given a topological space X, and a subset $S \subset X$, we can make S into a topological space by declaring that the open subsets of S are $U \cap S$ for open $U subset X$ This is called the subsapce topology

A subset S of a topological space X is clopen if it is both closed and open in X.(equivalent, both S and its complement are open)

Show that a space X has nontrivial clopen set(one other than $\emptyset and X if and only if X can be written as a disjoint union of two nonempty open sets$)

we say X is disconnected if there are nontrivial clopen sets, and connected  


A path in the space X is a continuous function $\gamma: [0,1] \to X$

A space X is path-connected if any two points in it are connected by some path

path-connected implies connected


homotopy: is the idea of continuous deformation 就是如果两个点之间会有很多种情况可以把他们连接在一起（如果中间没有洞），但如果中间有洞，你的连线方式就不一样了

然后定义homotopic

A space X is simply connected if it is path-connected and for any p and q ,all paths from p to q are homotopic(感觉是没洞)

a basis for a topological space X is a subset B of the open sets such that every open set in X is a union(possibly infinite) of some number of elements in B（感觉就是可以通过这些basis来组成every open set）


Compactness generalizes the notion of closed and bounded in Euclidean space to any topogical space

in metric spaces, there are two equivalent ways of formulating compactness:
A natural definition using sequences, called sequential compactness
A less natural definition using open covers

sometimes we think sequence in general topological spaces suck
so we use seconde defintion

A metric space M is sequentially compact if every sequence has a subsequence which converges

closed subsets of sequentially compact sets are compact

If X and Y are compact spaces, so is $X \times Y$

A subset of R^n is compact if and only if it is closed and bounded

An open cover of topological space X is a collection of open sets {U_a}(possibly infinite or uncoutable) which cover it: every point in X lies in at least one of the U_a so that $X= \cup U_a$

A topological space X is quasicompact if every open cover has a finite subcover. It is compact if it is also Hausdorff

A metric space M is sequentially compact if and only if it is compact

紧致性的概念帮助我们通过保证一个有限的开集子集仍然能够覆盖整个空间，从而简化了处理无限开集的复杂性，因为他提供了一种即使在处理无限集合时也能用有限数据工作的方式

If M is a compact metric space, then continuous functions $f:M \to N are continuous in an especially nice way$

A function $f:M \to N$ of metric spaces is called unifomrly continuous if for any $\epsilon \geq 0$ there exists a $\delta \geq 0 $(depending only on $\epsilon$) such that whenever $d_M(x,y) \leq \delta$ we also have $d_N(f(x),f(y)) < \epsilon$
we can have a $\delta$ that works for every point of M

If M is compact and $f:M \to N$ is continuous, then f is uniformly continuous

Heine Borel

For a metric space M, the following are equivalent: Every sequence has convergent subsequence<=>The space M is complete and totally bounded<=> Every open cover has a finite subcover

A closed subset of a compact set is compact(why so trivial but to prove)

现在我们要讨论就是如果是closed and bounded这个和compactness有什么关系

Consider the normed space $(\mathbb{R}^d,\|\cdot\|_2)$ ,the Euclidean space. In this space, S is compact if and only if S is closed and bounded

about nested rectangles

Let $((\mathbb{R}_i)(i\in N))$ be a sequence of nested closed rectangles.i.e , $R_{i+1} \subset R_i$ for all i $ \in N$ Then $\cap_{i \in N} R_i \neq \emptyset$

Heine-Borel Lemma. A closed rectangle in Euclidean space is compact(wiht the Euclidean norm)(还没看证明)

Sequential compactness
We saw in the previous section that compact sets in $\mathbb{R}^{n}$
can be characterized precisely as the closed and bounded sets.然后我们定义另一个valid characterization namely sequential compactness

闭且有界的集合不一定是紧致的，打破了有限维空间中“闭且有界即紧致”的直观认识。(在有限维空间中（如 $\mathbb{R}^n$ 
n
 ），海涅-博雷尔定理告诉我们闭且有界的集合是紧致的。
但在无限维空间中，这个结论不再成立。

In any metric space, a set is compact if and only if it is sequentially compact
（这里其实引入一个问题为什么我们不用这个definition来一开始定义compact，这是因为in topological
spaces, it is no longer true that all sequentially compact sets are compact）

Let (X,d) be a metric space. If $A \subset X$ is compact, then it is sequentially compact

A set D is said to be dense in a metric space (X, d) if every
point of $ X\D $ is a limit point of D, i.e. if X = $\bar{D}$.

we are especially interested in metric spaces that have countable dense subsets, we call them seperable

A metric (X,d) is seperable if it has a countable dense subset(可分空间的定义是：存在一个可数的稠密子集 DD，使得对于空间中的任意一个元素，都可以在 DD 中找到一个任意接近的元素。
换句话说，任意一个元素都能通过 DD 中的元素以任意精度进行逼近。)

无穷范数就是该向量各个分量的绝对值的最大值
dense(感觉也可以理解为在complement里面任意一个点附近画一个小圆那么这里面一定可以找的到一个dense集合的点)
它是稠密的意味着任何空间中的元素都可以通过可数集中的元素来逼近。对于有限维的空间，通常可以通过有限数量的向量来逼近空间中的任何点。然而，l-infinity
  空间中的元素是无穷多维的，因此空间结构变得复杂。

  关键思想：
$\ell^\infty$ 空间的基是由“标准基”（例如 $(1, 0, 0, 0, \dots)$）构成的，这些基向量并不具有紧凑性或简单的结构。
$\ell^\infty$ 空间有“太多的方向”，即每个序列的无穷分量可以自由变化，这样就产生了无穷多的方向。
因此，$\ell^\infty$ 空间中的元素不可能通过一个可数集来稠密覆盖整个空间。换句话说，即使我们选择一个可数集，它也无法在 $\ell^\infty$ 中“逼近”所有的元素。这个性质表明，$\ell^\infty$ 空间是不可数的，无法用一个可数集来覆盖。
它们在某些分量上会显著不同

If X is sequentially compact then (X, d) is separable.（这个证明的关键就是我们找到一个子集，这个子集可以覆盖整个X（这里构造了dense，因为都可以覆盖了那肯定是是在一个任意一个小ball里面肯定能找到dense的子集的点），而且这个子集是countable而且是dense的）（无非就是构造，证明是构造一个稠密的可数子集的过程，通常用于证明某些空间中可以通过可数集来稠密地覆盖整个空间）

你提到的一个思路是，我们可以从一个任意的开集覆盖 S 开始，然后通过基集来简化这个覆盖。由于任何开集都可以表示为基集的并集，我们可以将任意覆盖表示为基集的覆盖。在某些条件下（例如紧致性），我们甚至可以从中提取出有限子覆盖。

这一思想在拓扑学和分析中非常重要，特别是在处理紧致性时，因为紧致性保证了任何开覆盖都有有限的子覆盖（We consider any metric space (X, d). Then the set of open
balls of all radii around all points of X is a base.)
whenever we have a separable space, we can construct a countable base


Sequentially compact sets are compact.

稠密子集意味着空间 X 中的每一个点，要么是 D 的元素，要么是 D 的极限点。


Thinking again
about R, compact sets are closed and bounded there. It turns out that this is very
nearly true in complete metric spaces. It is not quite true because boundedness
is too weak in general.

we define $\epsilon$ set
and we define totally bounded

Totally bounded is a stronger condition than bounded, because it requires that the space can be covered by a finite number of balls of any given radius, whereas bounded only requires that there is a single ball that can contain the entire space.

totally bounded implies bounded

In $\mathbb{R}^n$ with any norm, bounded sets are totallyy bounded and vice-versa. This can be seen by considering the balls of radius 1 around each point of the set.

Finite sets in any metric space are totally bounded

In discrete metric space, finite sets are totally bounded but for all sets are bounded

Let (X, d) be a complete metric space. Then A ⊂ X is compact
if and only if A is closed and totally bounded.

A metric space is compact if and only if it is complete and
totally bounded.

全有界性： 只关注开球覆盖的问题，即用有限个小球去覆盖集合。
紧致性： 需要面对更广泛的“任意开集”覆盖，而不仅仅是小球覆盖。

然后我们定义continuous
we find that f is continuous at $x \in X$ if and only if for any sequence (x_n) in X that converges to a point $x \in X$ the sequence (f(x_n)) converges to f(x) in Y

but we find that this is not a good definition for topological space as it stills limit in the metric space

then we define the limit of a function in topological space

f is continuous from (X,d_X) to if and only if for any
open subset G ⊂ Y , the pre-image of G by f, f
−1
(G) = {x ∈ X : f(x) ∈ G}, is
open

Let (X, d_X), (Y, d_Y ) be metric spaces, and let f : X → Y be
continuous. If K ⊂ X is compact, then f(K) is compact in Y .

Lastly, recall that continuous real functions on closed bounded intervals are
bounded and attain their bounds. In metric spaces, compact spaces play the role
of closed bounded intervals, and so we expect a similar statement to hold. This
is indeed the case.(good intuition) as there exists a,b such that f(a)=sup f(x) and f(b)=inf f(x)

然后定义 uniformly continuous(which is for all $\epsilon >0$), there exists a $\delta >0$ such that whenever $d_X(x,y) < \delta$ we have $d_Y(f(x),f(y)) < \epsilon$ this is a stronger condition than continuity as it requires a single $\delta$ that works for all points in X(this is a global property)


Let (x,d_x) and (y,d_y) be metric spaces, and $k \subset X$ be compact. If $f:X \to Y$ is continuous, then f(K) is compact in Y

(this is a good intuition as we can use the compactness of K to find a finite subcover of any open cover of f(K))

every subset of a discrete metric space is open

对于 U 内的每个点 x，我们可以围绕它画一个足够小的球，这个球完全包含在 U 里。
如果这样的球总能找到，说明 U 的边界是“虚线的”，不包括边界点，所以 U 是开集。

Sequences of functions and uniform convergence

pointwise convergence: 就是我们常规的定义（我们不同的x决定不同的N）（收敛速率不同）

uniform convergence: 就是对于所有x，存在一个N，使得对于所有n>N，有|f_n(x)-f(x)|<$\epsilon$ 就是我们这个N和x无关的（收敛速率相同）
比如x^n在(0,1)上pointwise收敛，但是不uniform convergence 因为比如在x趋近于1的时候我的N是随着x改变的，因为如果我的x很小那么我收敛到0的速度就很快，但是如果x靠近1那么我收敛到0的速度就很慢所以这个东西取决于我们的x，所以就不是uniform convergence

因此我们定义Extended sup norm

and for proposition $f_n converges uniformly to f$ if and only if $sup_x|f_n(x)-f(x)| \to 0$ as $n \to \infty$


Let（X,d） be a metric space. If(f_n) is a sequence of functions from X to R such that $f_n \to f$ uniformly on X, and each f_n is continuous, then f is continuous

Central principle of uniform convergence: Let X be a set, then the sequence of functions(f_n) converges uniformly on X if and only if for every $\epsilon >0$ there exists an N such that for all $n,m\geq N$  we have $|f_n(x)-f_m(x)| < \epsilon$

Let (X,d) be a compact metric space. （C(X),||*||_{sup}) is a Banach space（这里用到了如果是一个complete那么就是cauchy列收敛，但是为啥这么定义就完备呢（柯西列强调序列内部的接近性。（因为cauchy列的定义里不包含收敛值，而complete就要求cauchy列能收敛到space里某个点，而closed set的意思是如果某个点是一个sequence的limit，那么这个点必然这个set里，从最严谨的角度来说，real number应该是这样定义的：把Q里所有的Cauchy sequence形成一个集合X，然后对于X里的xn、yn，称两者等价当且仅当for all epsilon>0 exists N s.t. n>N => |x_n-y_n|< $ \epsilon $，然后这些equivalence class就被称为real number）
收敛强调序列趋向于某个点。
完备空间中，柯西收敛与收敛等价。
非完备空间中，柯西列可能不收敛。（思考为什么这么定义，以及每个公式说明了啥，自己construct而不是接受）））




Show that
⟨(xn),(yn)⟩ := X∞
n=1
xnyn, (xn),(yn) ∈ ℓ
2
,
defines an inner product on ℓ
2
that induces the norm ∥ · ∥
（注意inner product的定义）




