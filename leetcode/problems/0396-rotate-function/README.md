# 396. Rotate Function

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/rotate-function/)

## Problem Description

You are given an integer array nums of length n.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.

## Approach

1. Once you decide where one element goes, the entire rotated array is determined because all elements shift together
2. Instead of computing each F(k) from scratch (which would be O(n²)), can you find a relationship between F(k) and F(k-1)? When you rotate by 1 position clockwise the last element coefficient becomes 0, all other coefficients get summed once more
3. If I calculate the sum of the coefficients of F(0) and i denote it as C and I calculate the sum of the array elements and i get S, this means that F(1) = F(0) + S - (last x len(arr)).
4. for any rotation k: F(k) = F(k-1) + S - n*arr[n-k]

## Complexity

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

## Notes

[Your notes]
