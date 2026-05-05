# 61. Rotate list

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/rotate-list/)

## Problem Description

Given the head of a linked list, rotate the list to the right by k places.

## Approach

After rotation, the last k nodes move to the front.  The two-pointer technique is a very elegant approach for finding the split point.
Fast pointer advances k steps from head. Slow starts from head.
Then both pointers move together until fast reaches the end.
Slow pointer will be at the partition point

You need to handle the case where k >= length. The two-pointer approach works well only if you first compute k % length, then apply the technique.

## Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Notes

[Your notes]
