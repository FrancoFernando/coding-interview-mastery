"""
LeetCode #3737: Count Subarrays With Majority Element I
Difficulty: Medium
Link: https://leetcode.com/problems/count-subarrays-with-majority-element-i/
"""
from typing import List
from itertools import accumulate


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # +1 where the element is target, -1 otherwise. A subarray has target as
        # its strict majority iff (#target) - (#non-target) > 0, i.e. its
        # transformed sum is positive.
        transformed = [1 if n == target else -1 for n in nums]

        # prefix[j] = sum of the first j transformed elements (prefix[0] = 0).
        # Subarray sum nums[i..j-1] = prefix[j] - prefix[i], so a subarray is
        # valid iff prefix[j] > prefix[i] for some i < j.
        prefix = list(accumulate(transformed, initial=0))

        result = 0
        for i in range(len(prefix)):
            for j in range(i + 1, len(prefix)):
                if prefix[j] > prefix[i]:
                    result += 1
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

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
