# Notes:
Search Problems:
- State space: the set of all states in the search problem
- Actions: the set of all actions that can be taken in the search problem
- Transition model: outputs the next state whena specific action is taken at current state
- Goal test: the condition that determines whether a given state is a goal state
- Action cost: incurred when moving from one state to another after applying an action

##  Fundamental counting principle:
- If there are n1 ways to do one thing, and n2 ways to do another, then there are n1 * n2 ways to do both.


## state space graph:
- Nodes: states
- Edges: actions
- Edge cost: action cost

search trees is more like a tree, where each node has multiple children.

tree search:
- Nodes: represent plans for reaching states
- complete: it finds a solution if we give it infinite computational resources
- optimal: it can find the least-cost path for the goal state

## 3 algorithms:
- BFS: Breadth-first search    BFS is generally not optimal because it simply does not take costs into consideration when determining which node to replace on the frontier. 
- DFS: Depth-first search   it may stuck in infinite loops if there are cycles in the state space graph.
- UCS: Uniform-cost search    UCS is the only optimal algorithm because it always expands the least-cost node on the frontier. While the other two algorithms do not consider the cost of actions.This is like a bfs with a priority queue and rotation.

we prefer bfs rather than dfs as the time complexity of bfs is lower it is O(b^d) while dfs is O(b^m) where b is the branching factor and m is the max depth of the search tree but d is usually smaller than m. Unless we do not have enough memory to store the frontier of bfs.

cons for three algorithms:
- explores options in every direction equally
- no information about the goal location    

similarities for three algorithms:
- bfs delete nodes from start
- dfs delete nodes from deepest point(end)
- ucs delete nodes from lowest cost(if we end up with a wall, we will not go in that direction, but we will go in the other direction,even if the cost is higher)

## but how to deal with the problem of ucs?
Intuition: We want to make something that can reflect how close we are to the goal state to some extent.
We introduce a new concept called heuristic to deal with the problem of ucs.
Basically, a heuristic function is a function that inputs a current state and outputs a corresponding estimate.
Specifically, We can use Manhattan distance in Pacman example（|x1 - x2| + |y1 - y2|）: why this work?
As we come closer, the manhattan distance will be smaller.
(but how is this idea really being come up with?):From my point of view,first we need to ask a question like what is the difference between different states with the goal state. Different states have different distances to the goal state intuitively.

This idea introduces two algorithms called greedy best-first search and A* search.
For greedy search, it is like a ucs with a heuristic function. But it is not optimal and complete.(it is like wow! we do not care about the cost at all, if it is closer just go in that direction)(it is like expanding a node that you think is closest to the goal state)(it emphasis on manhattan distance,meaning it tends to first move in a direction that is closest to the goal state,and then consider other directions)(this is the problem of greedy search)(how to solve it?): we can use A* search to solve it.
(inst.eecs.berkeley.edu/~cs188/sp24/assets/notes/cs188-sp24-note03.pdf)(the graph is good here)

A* is kind of like  we think whether we can combie the greedy search and ucs to some extent. As greedy search is good at finding the goal state but it is not optimal and complete, and ucs is optimal and complete but it is not good at finding the goal state. So we think whether we can combie the two to some extent.

ucs orders by path cost,donated as g(n)
greedy search orders by heuristic,donated as h(n)

A* search orders by the sum of path cost and heuristic,donated as f(n) = g(n) + h(n)


A* search is like a ucs with a heuristic function and a cost function. It is optimal and complete.


Uniform cost search also called Dijkstra's algorithm is a kind of like A* search but without heuristic function.    
both use priority queue to implement.

should we stop when we find the goal state?
- No, we should continue to search for the goal state until the frontier is empty.

a heuristic is admissible if it never overestimates the cost to reach the goal.

coming up with admissible heuristic IS MOST IMPORTANT.  (think about definition)

optimality of A* search:
we can prove it: 
assumption:
A* search is optimal if the heuristic function is admissible.
A is the optimal solution to the problem.
B is a suboptimal solution to the problem.
B is on the frontier of the search tree, we need to show that we will find A before B.
some ancestor n of A is on the path to B.
claim: n will be expanded before B.
1.f(n) <= f(A)
2.f(B) > f(A)
3.f(n) <= f(B)
all ancestors of n are expanded and removed from the frontier before B.
A expanded before B.
A* search is optimal


often, admissible heuristics are solutions to relaxed problems.(meaning no constraint)


local search:
- hill climbing(steepest ascent)){
    最速上升法
    problem: local maxima
}
stochastic hill climbing which is like hill climbing but with a random restart that can avoid local maxima(具体还不太理解)
random sideways move

- simulated annealing
    aims to combine ranom walk and hill-climbing to obtain a complete and efficient search
    the algorithm chooses among the neighbors of the current state with a probability that depends on the difference between the cost of the neighbors and the current state and a temperature parameter that decreases over time. '
    其实就是随机游走和最速上升法的结合，但是随机游走是带有概率的，这个概率是基于当前状态和邻居状态之间的差异以及一个温度参数，温度参数随着时间推移而减小。
- genetic algorithm
    -genetic algorithm begin as a population of random states,then iteratively apply selection,crossover,and mutation operators to evolve the population towards better states.
- tabu search
- local beam search
    -another variant of hill-climbing
    -首先是贪心搜索，然后贪心是选择概率最大的，但这样最后不能保证找到最优解，所以需要local beam search也就是一次性保存多个状态，然后从这些状态中选择概率最大的。（和transformer有关）
- iterated local search
