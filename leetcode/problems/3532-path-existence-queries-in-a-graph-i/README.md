# 3532. Path Existence Queries in a Graph I

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/path-existence-queries-in-a-graph-i/)

## Problem Description

You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n sorted in non-decreasing order, and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], determine whether there exists a path between nodes ui and vi.

Return a boolean array answer, where answer[i] is true if there exists a path between ui and vi in the ith query and false otherwise.

Example 1:

Input: n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]
Output: [true,false]

Example 2:

Input: n = 4, nums = [2,5,6,8], maxDiff = 2, queries = [[0,1],[0,2],[1,3],[2,3]]
Output: [false,false,true,true]

Constraints:

1 <= n == nums.length <= 10^5
0 <= nums[i] <= 10^5
nums is sorted in non-decreasing order.
0 <= maxDiff <= 10^5
1 <= queries.length <= 10^5
queries[i] == [ui, vi]
0 <= ui, vi < n

## Approach

A query asks whether `u` and `v` are in the same connected component (reachability in an
undirected graph means "same component").

Building every edge is O(n^2) and too slow. The key observation is that **nums is sorted**:
if `|nums[i] - nums[j]| <= maxDiff`, then every element between them is also within `maxDiff`
of its neighbors, so index `i` and `j` are already chained through consecutive edges. Therefore
only consecutive pairs matter.

Walk the array once and assign each index a component label, incrementing the label whenever the
gap between consecutive values exceeds `maxDiff`. Because the array is sorted, components are
contiguous runs of indices and are finalized in a single pass — no merging, so union-find is
unnecessary. Each query is then an O(1) label comparison.

## Complexity

- **Time Complexity:** O(n + q), where n = number of nodes and q = number of queries
- **Space Complexity:** O(n) for the component-label array
