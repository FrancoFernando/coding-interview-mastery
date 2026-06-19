# 1732. Find the Highest Altitude

**Difficulty:** Easy  
**Link:** [LeetCode](https://leetcode.com/problems/find-the-highest-altitude/)

## Problem Description

There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. The biker starts his trip on point `0` with altitude equal to `0`.

You are given an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between points `i` and `i + 1` for all `0 <= i < n`. Return the highest altitude of a point.

## Approach

The altitude at each point is a running prefix sum of `gain`. Walk the array, accumulate the prefix sum, and track the maximum.

Initialize `result = 0` to account for the starting point (altitude 0), so an all-downhill trip correctly returns 0.

The same idea expressed with `itertools.accumulate`: `max(0, max(accumulate(gain)))`.

## Complexity

- **Time Complexity:** O(n) — single pass over `gain`
- **Space Complexity:** O(1)

## Notes

This is the classic running-prefix-max pattern.
