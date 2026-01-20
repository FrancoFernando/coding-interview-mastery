# 1323. Maximum 69 Number

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/maximum-69-number/)

## Problem Description

You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:

Input: num = 9669
Output: 9969

Example 2:

Input: num = 9996
Output: 9999

Example 3:

Input: num = 9999
Output: 9999

Constraints:

1 <= num <= 104
num consists of only 6 and 9 digits.

## Approach

The maximum number we can obtain is by changing the leftmost '6' digit into a '9'. Converting the input to string makes things simpler.

## Complexity

- **Time Complexity:** O(n), where n is the number of digits
- **Space Complexity:** O(n)
