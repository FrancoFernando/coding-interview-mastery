"""
LeetCode #3739: Count Subarrays With Majority Element II
Difficulty: Hard
Link: https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
"""
from typing import List
from itertools import accumulate


class Fenwick:
    """Binary Indexed Tree (1-based). Supports point update and prefix-sum query,
    each in O(log n). Index 0 is unused."""

    def __init__(self, n: int):
        self.tree = [0] * (n + 1)

    def update(self, i: int, delta: int = 1) -> None:
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i  # move to the next node that covers i

    def query(self, i: int) -> int:
        """Sum of positions 1..i."""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i  # drop the lowest set bit to reach the next chunk
        return s


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # +1 where the element is target, -1 otherwise: target is the strict
        # majority of a subarray iff its transformed sum is positive.
        transformed = [1 if n == target else -1 for n in nums]

        # prefix[j] = sum of the first j transformed elements (prefix[0] = 0).
        # A subarray is valid iff prefix[j] > prefix[i] for some i < j, so the
        # answer is the number of pairs i < j with prefix[i] < prefix[j].
        prefix = list(accumulate(transformed, initial=0))

        # Prefix values lie in [-n, n]; offset them into [1, 2n+1] so they are
        # valid 1-based Fenwick indices.
        offset = len(nums) + 1

        def idx(v: int) -> int:
            return v + offset

        ft = Fenwick(2 * len(nums) + 1)
        result = 0
        for v in prefix:
            # how many already-seen prefixes are strictly less than v (i < j)
            result += ft.query(idx(v) - 1)
            ft.update(idx(v))
        return result


def test_solution():
    sol = Solution()

    assert sol.countMajoritySubarrays([1, 2, 2, 3], 2) == 5
    print("Test 1 passed: [1,2,2,3], target=2 -> 5")

    assert sol.countMajoritySubarrays([1, 1, 1, 1], 1) == 10
    print("Test 2 passed: all target -> 10")

    assert sol.countMajoritySubarrays([1, 2, 3], 4) == 0
    print("Test 3 passed: target absent -> 0")

    assert sol.countMajoritySubarrays([5], 5) == 1
    print("Test 4 passed: single target element -> 1")

    # Cross-check the O(n log n) Fenwick solution against the O(n^2) brute force.
    def brute(nums, target):
        count = 0
        for i in range(len(nums)):
            seen = 0
            for j in range(i, len(nums)):
                seen += 1 if nums[j] == target else 0
                if seen * 2 > (j - i + 1):
                    count += 1
        return count

    import random
    rng = random.Random(0)
    for _ in range(300):
        arr = [rng.randint(1, 4) for _ in range(rng.randint(1, 30))]
        t = rng.randint(1, 4)
        assert sol.countMajoritySubarrays(arr, t) == brute(arr, t), (arr, t)
    print("Test 5 passed: matches brute force on random inputs")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
