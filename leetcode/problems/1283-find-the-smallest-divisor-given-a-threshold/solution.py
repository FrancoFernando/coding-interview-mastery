"""
LeetCode #1283: Find the Smallest Divisor Given a Threshold
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""
import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def compute_sum(divisor: int) -> int:
            return sum(math.ceil(num / divisor) for num in nums)

        left, right = 1, max(nums)

        while left < right:
            mid = left + (right - left) // 2

            if compute_sum(mid) <= threshold:
                right = mid
            else:
                left = mid + 1

        return left
