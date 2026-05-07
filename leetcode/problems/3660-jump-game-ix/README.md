# 3660. Jump Game IX

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/jump-game-ix/)

## Problem Description

You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

Jump to index j where j > i is allowed only if nums[j] < nums[i].
Jump to index j where j < i is allowed only if nums[j] > nums[i].
For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

Return an array ans where ans[i] is the maximum value reachable starting from index i.

 

Example 1:

Input: nums = [2,1,3]

Output: [2,2,3]

Explanation:

For i = 0: No jump increases the value.
For i = 1: Jump to j = 0 as nums[j] = 2 is greater than nums[i].
For i = 2: Since nums[2] = 3 is the maximum value in nums, no jump increases the value.
Thus, ans = [2, 2, 3].

Example 2:

Input: nums = [2,3,1]

Output: [3,3,3]

Explanation:

For i = 0: Jump forward to j = 2 as nums[j] = 1 is less than nums[i] = 2, then from i = 2 jump to j = 1 as nums[j] = 3 is greater than nums[2].
For i = 1: Since nums[1] = 3 is the maximum value in nums, no jump increases the value.
For i = 2: Jump to j = 1 as nums[j] = 3 is greater than nums[2] = 1.

## Approach

1. from each index I can build a direct graph following forward and backward jumps. the graph can but up to n verticxes and n edges, so using bfs on each vertex takes O(N^3) time 

2. if i can do a backward jump from index j to index i then i can do a forward jump from index i to index j and vice versa, so the graph is actually undirected. The overall graph is made of connected components and the answer for each index in a component is the max in that component. 

3) union find can be used to find each component, but there is a more efficient approach

4) Is there structure in this graph that lets me find components without examining every pair? if nums\[i] and nums\[j] belong to the same component every nums\[k\] with i<k\<j belong to the same component. components are always contiguous intervals of indices

5) The  problem becomes "find the boundaries between consecutive components." Boundary at k ⟺ no crossing edge exists. max(nums\[0..k]) ≤ min(nums\[k+1..n-1]). prefix_max / suffix_min are the natural tools to verify this in constant time.

6) Walk through the array. Whenever prefix_max\[k] ≤ suffix_min\[k+1], you've found a boundary: segment ends at k, next segment starts at k+1.


## Complexity

- **Time Complexity:** O(N)
- **Space Complexity:** O(N)

## Notes

[Your notes]
