# 796. Rotate string

**Difficulty:** Easy  
**Link:** [LeetCode](https://leetcode.com/problems/rotate-string/)

## Problem Description

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.

## Approach

The brute force is to try all the possible shifts and compare against the goal but it's inefficient. You don't need to generate shifts.

 If you have string s = "abcde" and create s + s, all rotations of s appear as substrings in s + s.

 The in operator (or find) in Python uses an optimized string searching algorithm and solve the problem in linear time.

 Given the constraints even a simple O(n²) sliding window approach would be perfectly acceptable.
Just iterate through s + s and check each substring of length n against goal.

## Complexity

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

## Notes

[Your notes]
