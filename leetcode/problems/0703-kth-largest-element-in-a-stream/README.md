# 703. Kth Largest Element in a Stream

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## Problem Description

Implement the KthLargest class:

- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
- int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.

Example:

Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output: [null, 4, 5, 5, 8, 8]

Constraints:

0 <= nums.length <= 104
1 <= k <= nums.length + 1
-104 <= nums[i] <= 104
-104 <= val <= 104
At most 104 calls will be made to add.

## Approach

Use a min heap to keep the k largest elements. For each add, dequeue an element if it's smaller than the new one.

## Complexity

- **Time Complexity:** O(log k) for each add operation
- **Space Complexity:** O(k) for the heap
