# 322. Coin Change

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/coin-change/)

## Problem Description

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

## Approach

Use dynamic programming where dp[i] represents the minimum number of coins needed to make amount i.
For each amount from 1 to target, try all coins and take the minimum.

## Complexity

- **Time Complexity:** O(amount * n), where n is the number of coins
- **Space Complexity:** O(amount)
