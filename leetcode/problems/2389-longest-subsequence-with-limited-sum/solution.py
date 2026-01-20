"""
LeetCode #2389: Longest Subsequence With Limited Sum
Difficulty: Easy
Link: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
"""
import bisect
from itertools import accumulate
from typing import List


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort and compute prefix sums
        nums.sort()
        prefix_sum = list(accumulate(nums))

        # For each query, find the longest subsequence
        result = []
        for query in queries:
            # bisect_right gives the insertion point (= count of elements <= query)
            result.append(bisect.bisect_right(prefix_sum, query))

        return result
