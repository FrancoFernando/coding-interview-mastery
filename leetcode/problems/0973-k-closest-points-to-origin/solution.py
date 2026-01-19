"""
LeetCode #973: K Closest Points to Origin
Difficulty: Medium
Link: https://leetcode.com/problems/k-closest-points-to-origin/
"""
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Max heap (negate distance) to keep k closest points
        heap = []

        for x, y in points:
            dist = -(x * x + y * y)  # Negate for max heap behavior

            if len(heap) < k:
                heapq.heappush(heap, (dist, x, y))
            elif dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, x, y))

        return [[x, y] for _, x, y in heap]
