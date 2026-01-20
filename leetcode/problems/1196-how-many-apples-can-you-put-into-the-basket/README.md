# 1196. How Many Apples Can You Put into the Basket

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/)

## Problem Description

You have some apples and a basket that can carry up to 5000 units of weight.

Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you can put in the basket.

Example 1:

Input: weight = [100,200,150,1000]
Output: 4

Example 2:

Input: weight = [900,950,800,1000,700,800]
Output: 5

Constraints:

1 <= weight.length <= 103
1 <= weight[i] <= 103

## Approach

To maximize the number of apples we need to pick the ones with minor weight first. Sorting the input array is how to do it.

## Complexity

- **Time Complexity:** O(n log n) due to sorting
- **Space Complexity:** O(1)
