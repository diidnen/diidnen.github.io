## If x is a limit point of A,then such a sequence $(y_n)$ exists.
#### Definition of a limit point: x is a limit point of A if every open ball B(x,r) centered at x contains a point of A distinct from x.

#### Constructing the sequence: For each $n\in \mathbb{N}$,consider the open ball B(x,1/n).Since x is a limit point of A, there exists a point $y_n \in A$ such that $y_n \in B(x,1/n)$ and $y_n \neq x$. This gives a construction of the sequence $(y_n)$ in A with $y_n \neq x$   

#### finally we want to prove that $(y_n)$ is convergent. For any $\epsilon>0$ , choose $N \in \mathbb{N}$ such that $\frac{1}{N} < \epsilon$. Then for all $n \geq N$, $d(y_n,x)<\frac{1}{n} \leq \frac{1}{N} < \epsilon$. Thus ,$y_{n}\rightarrow x$

## If such a sequence $(y_n)$ exists  , then x is a limit of A.
#### Existence of the sequence: Suppose there exists a sequence $(y_n)$ in A such that $y_n \rightarrow x$ and $y_{n} \neq x$ for all n

#### Verifying the limit point condition: For any r>0, since $y_{n} \rightarrow x$, there exists N $\in \mathbb{N}$ such that for all n $n > N$, $d(y_n,x)<r$.In particular $y_{n+1} \in B(x,r)$ and $y_{n+1} \in A$ with $y_{n+1} \neq x$ so this is the point we can always find in the ball.

#### In conclusion, Since r>0 is arbitrary, x is a limit point of A.



 
1.(Definition: If (S,d) is complete $\Rightarrow$ every cauchy sequence converges in S; 
Consider all limit points of S, and $\forall$ limit points(called them to be  $x \in S$ ) we can find a seqeunce $y_n$ such that $y_{n}\rightarrow x$, and as (S,d) is complete,then the sequence converges to unique x and x is in S so S is closed) 

2.(If $S$ is closed, then it contains all limit points, and as $(X,d)$ is complete so every cauchy sequence in $X$ converges, so take an arbitrary cauchy sequence in $S$ to be $y_n$, and as the cauchy sequeunce is in $X$ so it converges to a value in $X$, and as $S$ is closed, the convergent value is in $S$, therefore $\forall$ cauchy sequence in $S$, they converge to a value in $S$, so $S$ is complete)


First by slides: $\bar{\bar{A}}$=$\bar{A}$ if and only if $\bar{A}$ is closed
so we want to prove $\bar{A}$ is closed:
that means $\bar{A}$ contains all its limit points.And $\bar{A}$'s limit points are either from sequences with infinitely many terms of ${x_n}$ are in A or only finitely many terms of ${x_n}$ are in A.

Case 1(sequences with infinitely many terms of ${x_n}$ are in A):since $\bar{A}$ is the union of A and A's limit points,so if it in this case, so each of these sequences will converges to a unique limit points of A(called it to be x), and since $\bar{A}$ is the union of A and A's limit points, so x is also in $\bar{A}$

Case 2(sequences with only finitely many terms of ${x_n}$ are in A): there exists N such that for all $n \geq N$, $x_n \in A'$(the set of limit points of A) since $x_n \in A'$, there exists a sequence ${y_{n,m}}$ in A such that  ${y_{n,m}}$ ->x_n as m->infinity
and we can take N>0 such that $\forall$ m>N, we can make the sequence ${y_{n,m}}$ as close as to x_n, and similarly we can find $N_1$ such that $\forall$ n>$N_1$ we can make x_n as close to the limit point x, so we can take max{N,N_1} to make the sequence  ${y_{n,m}}$ converges to x and as ${y_{n,m}}$ is a sequence in A so it converges to a point in $\bar{A}$