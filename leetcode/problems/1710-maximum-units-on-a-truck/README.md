# 1710. Maximum Units on a Truck

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/maximum-units-on-a-truck/)

## Problem Description

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi].

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.

Return the maximum total number of units that can be put on the truck.

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8

Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106

## Approach

To maximize the number of units, put boxes with more units on the truck first.
Sorting the types of boxes by number of units makes this straightforward.
Optimization: for each type of box, take the maximum allowed by the remaining capacity.

## Complexity

- **Time Complexity:** O(n log n) due to sorting
- **Space Complexity:** O(1)
