"""
LeetCode #1196: How Many Apples Can You Put into the Basket
Difficulty: Easy
Link: https://leetcode.com/problems/how-many-apples-can-you-put-into-the-basket/
"""
from itertools import accumulate
from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        cumulative_weights = list(accumulate(sorted(weight)))

        for i, total_weight in enumerate(cumulative_weights):
            if total_weight > 5000:
                return i

        return len(weight)
