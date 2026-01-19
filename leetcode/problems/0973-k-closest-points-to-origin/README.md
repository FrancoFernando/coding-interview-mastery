# 973. K Closest Points to Origin

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin/)

## Problem Description

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance.

Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]

Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104

## Approach

Iterate through the array of points and keep the k closest to the origin.
A max heap is the ideal data structure for this. Elements are the points and priority is the distance to the origin.

## Complexity

- **Time Complexity:** O(n log k), where n is the number of points
- **Space Complexity:** O(k) for storing the k closest points in the heap
