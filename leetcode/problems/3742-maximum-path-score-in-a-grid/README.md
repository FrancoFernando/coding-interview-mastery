# 3742. Maximum Path Score in a Grid

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/maximum-path-score-in-a-grid/)

## Problem Description

You are given an m x n grid where each cell contains one of the values 0, 1, or 2. You are also given an integer k.

You start from the top-left corner (0, 0) and want to reach the bottom-right corner (m - 1, n - 1) by moving only right or down.

Each cell contributes a specific score and incurs an associated cost, according to their cell values:

0: adds 0 to your score and costs 0.
1: adds 1 to your score and costs 1.
2: adds 2 to your score and costs 1. ​​​​​​​
Return the maximum score achievable without exceeding a total cost of k, or -1 if no valid path exists.

Note: If you reach the last cell but the total cost exceeds k, the path is invalid.

## Approach

Step 1: Why DP?

You move only right or down on a grid. The number of paths is exponential, so you can't enumerate them all. But every path to (i,j) comes from either (i-1,j) or (i,j-1): overlapping subproblems, optimal substructure. Textbook DP.
Without cost limits: dp[i][j] = score[i][j] + max(dp[i-1][j], dp[i][j-1])

Step 2: Why a 2D DP fails

A single number per cell isn't enough state. You need to remember score as a function of cost spent so far.

Step 3: The 3D DP
Adding cost as a dimension:

dp[i][j][c] = max score reachable at cell (i,j) having spent exactly cost c

Which is the transition between states?
Let s = score(v), cost_v = cost(v), where v = grid[i][j]
dp[i][j][c] = s + max( dp[i-1][j][c - cost_v], dp[i][j-1][c - cost_v] )

The answer is the max score reachable at cell (m - 1, n - 1) when the cost is 0...k: 
max(dp[m-1][n-1][c]) for c in 0..k.

Implementation details

- Skip transitions where c - cost_v < 0, i < 0, j < 0
- Top row (i = 0, j > 0): can only come from the left.
- Left column (j = 0, i > 0): can only come from above


That's the whole solution. Complexity: O(m · n · k).


## Complexity

- **Time Complexity:** O(nmk)
- **Space Complexity:** O(nmk)

## Notes

[Your notes]
