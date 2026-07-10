# 3534. Path Existence Queries in a Graph II

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/)

## Problem Description

You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], find the minimum distance between nodes ui and vi. If no path exists between the two nodes, return -1 for that query. The edges are unweighted.

Return an array answer, where answer[i] is the result of the ith query.

Example 1:

Input: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]
Output: [1,1]

Example 2:

Input: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]
Output: [1,2,-1,1]

Example 3:

Input: n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]
Output: [0,-1,-1]

Constraints:

1 <= n == nums.length <= 10^5
0 <= nums[i] <= 10^5
0 <= maxDiff <= 10^5
1 <= queries.length <= 10^5
queries[i] == [ui, vi]
0 <= ui, vi < n

## Approach

Unlike part I, `nums` is **not** sorted and we need the shortest distance, not just
connectivity. Sort the nodes by value first — then a node's neighbours (values within
`maxDiff`) form a **contiguous window** of sorted positions, turning the graph into a
"jump game."

1. **Sort by value.** Build `order` (sorted position -> original index) and its inverse
   `pos` (original index -> sorted position).
2. **Connectivity.** As in part I, contiguous runs of sorted values with consecutive
   gaps `<= maxDiff` form one component. If `u` and `v` are in different components, the
   answer is `-1`.
3. **One-jump reach.** `R[p]` = farthest sorted position reachable from `p` in a single
   edge. Because values are sorted, the right boundary is monotonic, so `R` is built with
   a single two-pointer pass in O(n).
4. **Binary lifting (a.k.a. binary jumping / sparse table).** `up[k][p]` = farthest
   position reachable from `p` in `2^k` jumps, with `up[k][p] = up[k-1][up[k-1][p]]`.
5. **Query.** Map `u, v` to sorted positions `a <= b`. Greedily take the largest
   power-of-two jumps that still fall short of `b`, then one final jump lands on it; the
   total jump count is the shortest distance. `a == b` gives `0`.

Greedily jumping as far right as possible is optimal because each edge reaches a
contiguous interval (the Jump Game II argument).

## Complexity

- **Time Complexity:** O((n + q) log n), where n = nodes and q = queries
- **Space Complexity:** O(n log n) for the binary-lifting table
