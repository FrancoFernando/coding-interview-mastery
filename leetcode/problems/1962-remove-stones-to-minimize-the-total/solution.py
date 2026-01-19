"""
LeetCode #1962: Remove Stones to Minimize the Total
Difficulty: Medium
Link: https://leetcode.com/problems/remove-stones-to-minimize-the-total/
"""
import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Max heap (negate values)
        heap = [-p for p in piles]
        heapq.heapify(heap)

        for _ in range(k):
            # Pop largest pile (negated)
            largest = -heapq.heappop(heap)
            # Remove floor(pile/2) stones
            remaining = largest - largest // 2
            # Push back (negated)
            heapq.heappush(heap, -remaining)

        return -sum(heap)
