# 215. Kth Largest Element in an Array

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Problem Description

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

## Approach

Use a min heap to store the largest k numbers. Every time a number is greater than the smallest in the heap, remove the smallest and insert the new one.

## Complexity

- **Time Complexity:** O(N log K) to insert N numbers into a heap of size K
- **Space Complexity:** O(K) for the heap
