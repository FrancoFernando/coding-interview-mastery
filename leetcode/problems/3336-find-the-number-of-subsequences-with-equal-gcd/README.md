# 3336. Find the Number of Subsequences With Equal GCD

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/)

## Problem Description

You are given an integer array nums.

Find the number of pairs of non-empty subsequences (seq1, seq2) of nums such that:

- seq1 and seq2 are disjoint (no index of nums is shared between them).
- The GCD of the elements of seq1 equals the GCD of the elements of seq2.

Return the total number of such pairs modulo 10^9 + 7.

Example 1:

Input: nums = [1,2,3,4]
Output: 10

Example 2:

Input: nums = [10,20,30]
Output: 2

Example 3:

Input: nums = [1,1,1,1]
Output: 50

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 200

## Approach

Each element has exactly three fates: go into `seq1`, into `seq2`, or into neither. A pair
of disjoint subsequences is therefore just a **3-way labelling** of the elements (the
"disjoint" condition is automatic). The pairs are ordered — `(A, B)` and `(B, A)` count
separately.

GCD is incremental, so the only state we need while processing elements is the running gcd
of each side. Any subset's gcd divides its elements, so gcd values are bounded by
`max(nums) <= 200`, giving a small `(M+1) x (M+1)` DP grid.

- `dp[g1][g2]` = number of labellings of processed elements leaving `seq1` with gcd `g1`
  and `seq2` with gcd `g2`.
- Use `0` as the "empty side" sentinel, exploiting `gcd(0, a) = a` so an empty side
  becomes its first real gcd with no special-casing. Start `dp[0][0] = 1`.
- For each element `a`, copy the grid (the "neither" choice), then add the "into seq1"
  (`g1 -> gcd(g1, a)`) and "into seq2" (`g2 -> gcd(g2, a)`) transitions, reading from the
  old grid and writing to the new one to avoid double counting.
- Both sides must be non-empty (`g >= 1`) with equal gcd, so the answer is the diagonal
  `sum(dp[g][g] for g in 1..M)`, taken modulo `10^9 + 7`.

## Complexity

- **Time Complexity:** O(n * M^2), where n = len(nums) and M = max(nums)
- **Space Complexity:** O(M^2) for the DP grid
