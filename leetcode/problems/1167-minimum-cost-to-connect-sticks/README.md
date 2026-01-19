# 1167. Minimum Cost to Connect Sticks

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)

## Problem Description

You have some number of sticks with positive integer lengths. These lengths are given as an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Example 1:

Input: sticks = [2,4,3]
Output: 14
Explanation: Combine 2 and 3 for cost 5, then 5 and 4 for cost 9. Total = 14.

Example 2:

Input: sticks = [1,8,3,5]
Output: 30

Constraints:

1 <= sticks.length <= 104
1 <= sticks[i] <= 104

## Approach

Simulate the process of joining each time the two shorter sticks. A min heap is the perfect data structure for this.

## Complexity

- **Time Complexity:** O(n log n), where n is the number of sticks, due to the heap operations
- **Space Complexity:** O(n) for storing all sticks in the heap
