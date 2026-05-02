# 788. Rotated Digits

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/rotated-digits/)

## Problem Description

An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].

## Approach

You don't need to actually construct the rotated number. You only need to check two conditions:

- No invalid digits (3, 4, 7) → if found, skip the number
- At least one changing digit (2, 5, 6, 9) → ensures the rotated number is different

## Complexity

- **Time Complexity:** O(nd), where di are digit per number
- **Space Complexity:** O(d) if converted tostring

## Notes

[Your notes]
