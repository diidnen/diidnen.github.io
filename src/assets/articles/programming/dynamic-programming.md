 # Dynamic Programming Explained

## What is Dynamic Programming?

Dynamic Programming (DP) is a method for solving complex problems by breaking them down into simpler subproblems.

### Key Concepts:
1. Optimal Substructure
2. Overlapping Subproblems

## Classic Examples

### Fibonacci Sequence

<pre><code class="javascript">// Fibonacci implementation using DP
const fibonacci = (n) => {
    const dp = new Array(n + 1);
    dp[0] = 0;
    dp[1] = 1;
    
    for(let i = 2; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    
    return dp[n];
}

// Example usage:
console.log(fibonacci(10));  // Output: 55</code></pre>

### Knapsack Problem

The 0/1 knapsack problem is a classic example of dynamic programming.

<pre><code class="javascript">/**
 * 0/1 Knapsack Problem Solution
 * @param {number[]} values - Array of item values
 * @param {number[]} weights - Array of item weights
 * @param {number} capacity - Knapsack capacity
 * @returns {number} Maximum value possible
 */
const knapsack = (values, weights, capacity) => {
    const n = values.length;
    const dp = Array(n + 1).fill()
        .map(() => Array(capacity + 1).fill(0));
    
    for(let i = 1; i <= n; i++) {
        for(let w = 0; w <= capacity; w++) {
            if(weights[i-1] <= w) {
                dp[i][w] = Math.max(
                    values[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                );
            } else {
                dp[i][w] = dp[i-1][w];
            }
        }
    }
    
    return dp[n][capacity];
}

// Example usage:
const values = [60, 100, 120];
const weights = [10, 20, 30];
const capacity = 50;
console.log(knapsack(values, weights, capacity));  // Output: 220</code></pre>