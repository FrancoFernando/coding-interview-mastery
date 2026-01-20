"""
LeetCode #1338: Reduce Array Size to The Half
Difficulty: Medium
Link: https://leetcode.com/problems/reduce-array-size-to-the-half/
"""
from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Count frequencies and sort in descending order
        freq = Counter(arr)
        sorted_freq = sorted(freq.values(), reverse=True)

        target = len(arr) // 2
        removed = 0
        count = 0

        for f in sorted_freq:
            removed += f
            count += 1
            if removed >= target:
                return count

        return count
