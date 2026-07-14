"""
LeetCode #3336: Find the Number of Subsequences With Equal GCD
Difficulty: Hard
Link: https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

Idea
----
Every element has exactly three fates: go into seq1, into seq2, or into neither.
So a pair of disjoint subsequences is just a 3-way labelling of the elements.

GCD is incremental (gcd of a growing set = gcd(running, new)), so the only state we
need is the running gcd of each side. Since any subset's gcd divides its elements,
gcd values are bounded by max(nums) <= 200 -> a tiny (M+1) x (M+1) grid.

dp[g1][g2] = number of labellings of the processed elements leaving seq1 with gcd g1
and seq2 with gcd g2. We use 0 as the "empty" sentinel because gcd(0, a) = a, so an
empty side turns into its first real gcd automatically. A side is non-empty iff its
gcd index is >= 1, so the answer sums the diagonal dp[g][g] for g >= 1.

Complexity: O(n * M^2) time, O(M^2) space, where M = max(nums).
"""
from math import gcd
from typing import List


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        M = max(nums)

        # g == 0 means "this side is still empty".
        dp = [[0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1

        for a in nums:
            ndp = [row[:] for row in dp]  # choice 3: put `a` in neither
            for g1 in range(M + 1):
                row = dp[g1]
                for g2 in range(M + 1):
                    v = row[g2]
                    if v:
                        # choice 1: put `a` in seq1
                        ndp[gcd(g1, a)][g2] = (ndp[gcd(g1, a)][g2] + v) % MOD
                        # choice 2: put `a` in seq2
                        ndp[g1][gcd(g2, a)] = (ndp[g1][gcd(g2, a)] + v) % MOD
            dp = ndp

        # Both sides non-empty (g >= 1) and equal gcd -> the diagonal.
        return sum(dp[g][g] for g in range(1, M + 1)) % MOD
