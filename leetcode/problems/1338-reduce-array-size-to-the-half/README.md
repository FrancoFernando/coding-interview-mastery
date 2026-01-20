# 1338. Reduce Array Size to The Half

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/reduce-array-size-to-the-half/)

## Problem Description

You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5.

Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1

Constraints:

2 <= arr.length <= 105
arr.length is even.
1 <= arr[i] <= 105

## Approach

The problem can be solved using a combo of data structures:
- Dictionary to count frequencies
- Priority queue to extract the greatest frequencies first

## Complexity

- **Time Complexity:** O(n log n), where n is the length of the input array
- **Space Complexity:** O(n) in the worst case if all elements are unique
