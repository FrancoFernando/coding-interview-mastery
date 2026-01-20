# 1283. Find the Smallest Divisor Given a Threshold

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)

## Problem Description

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element.

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5

Example 2:

Input: nums = [44,22,33,11,1], threshold = 5
Output: 44

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 106
nums.length <= threshold <= 106

## Approach

The possible divisors for the solution are between 1 and the maximum number in nums.
Use binary search to find the smallest divisor.

## Complexity

- **Time Complexity:** O(n log m), where n is the length of nums and m is the maximum value in nums
- **Space Complexity:** O(1)
