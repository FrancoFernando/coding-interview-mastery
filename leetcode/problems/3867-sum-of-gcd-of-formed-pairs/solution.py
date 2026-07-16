"""
LeetCode #3867: Sum of GCD of Formed Pairs
Difficulty: Medium
Link: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
"""
from typing import List
from math import gcd


class Solution:
    def sumGcdPairs(self, nums: List[int]) -> int:
        # prefixGcd[i] = gcd(nums[i], max(nums[0..i])), built with a running max.
        prefix_gcd = []
        mx = 0
        for x in nums:
            mx = max(mx, x)
            prefix_gcd.append(gcd(x, mx))

        prefix_gcd.sort()

        # Pair smallest with largest via two pointers. For odd n, lo and hi meet
        # at the middle (lo == hi) and it stays unpaired -- the "ignore middle" rule.
        lo, hi = 0, len(prefix_gcd) - 1
        total = 0
        while lo < hi:
            total += gcd(prefix_gcd[lo], prefix_gcd[hi])
            lo += 1
            hi -= 1
        return total


def test_solution():
    sol = Solution()

    assert sol.sumGcdPairs([2, 6, 4]) == 2
    print("Test 1 passed: [2,6,4] -> 2")

    assert sol.sumGcdPairs([3, 6, 2, 8]) == 5
    print("Test 2 passed: [3,6,2,8] -> 5")

    assert sol.sumGcdPairs([5]) == 0
    print("Test 3 passed: single element -> 0 (no pair)")

    assert sol.sumGcdPairs([4, 4]) == 4
    print("Test 4 passed: [4,4] -> gcd(4,4) = 4")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
