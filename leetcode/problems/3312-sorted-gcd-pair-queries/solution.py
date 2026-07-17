"""
LeetCode #3312: Sorted GCD Pair Queries
Difficulty: Hard
Link: https://leetcode.com/problems/sorted-gcd-pair-queries/
"""
from typing import List
from bisect import bisect_right


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # There are up to ~n^2/2 pairs, far too many to enumerate. Values are
        # small, so count how many pairs have each gcd via divisor
        # inclusion-exclusion.
        maxv = max(nums)
        freq = [0] * (maxv + 1)
        for x in nums:
            freq[x] += 1

        # exact[g] = number of pairs whose gcd is exactly g.
        # Pairs whose gcd is a MULTIPLE of g = C(#nums divisible by g, 2);
        # subtract exact counts of 2g, 3g, ... (processed first, top-down).
        exact = [0] * (maxv + 1)
        for g in range(maxv, 0, -1):
            d = 0
            for m in range(g, maxv + 1, g):
                d += freq[m]
            pairs = d * (d - 1) // 2
            for m in range(2 * g, maxv + 1, g):
                pairs -= exact[m]
            exact[g] = pairs

        # prefix[g] = number of pairs with gcd <= g (this is sorted gcdPairs,
        # run-length encoded). Non-decreasing with prefix[0] = 0.
        prefix = [0] * (maxv + 1)
        for g in range(1, maxv + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        # answer[i] = smallest g with prefix[g] > queries[i]
        return [bisect_right(prefix, q) for q in queries]


def test_solution():
    sol = Solution()

    assert sol.gcdValues([2, 3, 4], [0, 2, 2]) == [1, 2, 2]
    print("Test 1 passed: [2,3,4], queries [0,2,2] -> [1,2,2]")

    assert sol.gcdValues([4, 4, 2, 1], [5, 3, 1, 0]) == [4, 2, 1, 1]
    print("Test 2 passed: [4,4,2,1] -> [4,2,1,1]")

    # Cross-check against brute force on random inputs.
    from math import gcd
    from itertools import combinations
    import random

    def brute(nums, queries):
        gp = sorted(gcd(a, b) for a, b in combinations(nums, 2))
        return [gp[q] for q in queries]

    rng = random.Random(1)
    for _ in range(500):
        n = rng.randint(2, 15)
        nums = [rng.randint(1, 20) for _ in range(n)]
        npairs = n * (n - 1) // 2
        queries = [rng.randrange(npairs) for _ in range(rng.randint(1, 5))]
        assert sol.gcdValues(nums, queries) == brute(nums, queries), (nums, queries)
    print("Test 3 passed: matches brute force on 500 random cases")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
