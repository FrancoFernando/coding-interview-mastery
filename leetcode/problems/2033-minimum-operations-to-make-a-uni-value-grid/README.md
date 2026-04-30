# 2033. Minimum Operations to Make a Uni-Value Grid

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/)

## Problem Description

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

## Approach

1: check if divisible per X
2: if yes sort and pich the middle
3 count how many operation middle-current/x

## Complexity

- **Time Complexity:** O(nmlognm)
- **Space Complexity:** O(nm)

## Notes

[Your notes]
