"""
LeetCode #1979: Find Greatest Common Divisor of Array
Difficulty: Easy
Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
"""
from typing import List
from math import gcd


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # math.gcd is the Euclidean algorithm: O(log(min * max)).
        return gcd(min(nums), max(nums))


def test_solution():
    sol = Solution()

    assert sol.findGCD([2, 5, 6, 9, 10]) == 2
    print("Test 1 passed: min 2, max 10 -> 2")

    assert sol.findGCD([7, 5, 6, 8, 3]) == 1
    print("Test 2 passed: min 3, max 8 -> 1")

    assert sol.findGCD([3, 3]) == 3
    print("Test 3 passed: equal min/max -> 3")

    assert sol.findGCD([1, 1000]) == 1
    print("Test 4 passed: coprime extremes -> 1")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
