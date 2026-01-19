"""
LeetCode #1167: Minimum Cost to Connect Sticks
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-cost-to-connect-sticks/
"""
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        total_cost = 0

        while len(sticks) > 1:
            # Pop two smallest sticks
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)

            # Combine them
            combined = first + second
            total_cost += combined

            # Push combined stick back
            heapq.heappush(sticks, combined)

        return total_cost
