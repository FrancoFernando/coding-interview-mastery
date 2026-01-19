# 1962. Remove Stones to Minimize the Total

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)

## Problem Description

You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.

Return the minimum possible total number of stones remaining after applying the k operations.

Example 1:

Input: piles = [5,4,9], k = 2
Output: 12

Example 2:

Input: piles = [4,3,6,7], k = 3
Output: 12

Constraints:

1 <= piles.length <= 105
1 <= piles[i] <= 104
1 <= k <= 105

## Approach

Simulate the process of greedily picking the greatest pile and removing stones from it.
A max heap is the perfect data structure for this.

## Complexity

- **Time Complexity:** O(n log n + k log n), where n is the number of piles
  - O(n log n) for building the initial heap
  - O(k log n) for k operations on the heap
- **Space Complexity:** O(n) for the heap
