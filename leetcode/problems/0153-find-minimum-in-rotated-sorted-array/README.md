# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Problem Description

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.

## Approach

Compare nums[mid] to nums[right]:

- nums[mid] > nums[right] → pivot is to the right, min is in (mid, right], so left = mid + 1.
- nums[mid] < nums[right] → mid is in the "sorted upper run" with right, min is in [left, mid], so right = mid.

Why compare with right and not left? Because nums[mid] > nums[left] is ambiguous:it's true both for an unrotated [1,2,3,4,5] and a rotated [3,4,5,1,2], so you can't decide which side holds the min.

Use the left comparison is also possible, but you need to add add an "already sorted" early exit.

## Complexity

- **Time Complexity:** O(logN)
- **Space Complexity:** O(1)

## Notes

[Your notes]
