# Dual Space(notes)
First, we define linear form(linear functional): it is a map from a vector space(F-vector space) to F (e.g. real numbers) such that:
- $f(0) = 0$
- $f(x+y) = f(x) + f(y)$
- $f(ax) = af(x)$

F as a vector space over F.

And then we define dual space: it is the vector space of all linear functionals on V.

$V^* = L(V,F) = \{\theta: V \to F \mid \theta \text{ is linear}\}$
(here is F vector space remember!!!)
suffices to say where the basis(we need to emphasize on two things here, the first is that we need to define a map from a vector space and a vector space and then define dual space which are the linear maps from a vector spcae tod another space)

for linear maps, we only care about its basis, as it 
suffices to say where the basis elements are mapped to.

idea in proposition 3.3: we construct a dual space and prove a basis of it by proving linear independence and spanning.
Question: (looking at notes of proposition 3.3) why can we say that if $a_i = f(e_i)$, then $f = \sum_i a_i\epsilon_i$?

Corollary 3.4: If $V$ is finite-dimensional, then $V^*$ is finite-dimensional, and $\dim V^* = \dim V$.
(seems to be useful)

annihilator of U: $U^0 = \{f \in V^* \mid f(u) = 0, \forall u \in U\}$



(how to guarantee the transformation to be linear functions (example 1.6))

(why is it useful to define annihilator?)
(so spanning set should be finite?)


We now introduce a link between subspaces of $V$ and subspaces of $V^*$.

next we introduce annihilator of U, which is the set of all linear functionals that vanish on U.
And reversely, we can define the annihilator of a set of linear functionals, which is the set of all vectors that are mapped to 0(orthogonal??) by all the linear functionals.

check the step to find the annihilator of a set of vectors: the main idea is to find the linear functionals that vanish on the set of vectors. so we can find the linear combination that makes the linear functionals vanish on the set of vectors.

and also we can find the annihilator of a set of linear functionals by finding the vectors that are mapped to 0 by all the linear functionals.(which is also the kernal of the linear functionals)

and then we can introduce the rank-nullity theorem for the linear transformation between the dual spaces: We first consider a map $f: V^* \to U^*$. adn the key here is to proof the map is surjective(as we need to guarantee that any $U^*$ has a preimage in $V^*$). Next $kerf=U^0$, and by rank-nullity theorem, we have $dimV^* = dimU^* + dimU^0$.(As $kerf=U^0$, we have $dimU= dimU^*$).(so this tells us that the dimension of the dual space is the same as the dimension of the subspace.)


Dual maps:
consider a map $T: V \to W$, then we can define its dual map to be $T^*: W^* \to V^*$ is given by $\theta \mapsto \theta*T$(where $T$ is the linear map of $L(V,W)$).
(the dual map is a another type of dual space when we talk about matrix)
why define something like this?






