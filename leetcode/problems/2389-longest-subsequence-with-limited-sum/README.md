# 2389. Longest Subsequence With Limited Sum

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/longest-subsequence-with-limited-sum/)

## Problem Description

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]

Example 2:

Input: nums = [2,3,4,5], queries = [1]
Output: [0]

Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 106

## Approach

- For a subsequence, the order of the elements doesn't matter -> sort the input
- Sorting allows taking smaller elements first which maximizes the subsequence length
- Binary search can speed up each query using prefix sums

## Complexity

- **Time Complexity:** O(n log n + m log n), where n is the length of nums and m is the length of queries
- **Space Complexity:** O(n) for the prefix sum array
