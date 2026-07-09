"""
LeetCode #3532: Path Existence Queries in a Graph I
Difficulty: Medium
Link: https://leetcode.com/problems/path-existence-queries-in-a-graph-i/
"""
from itertools import pairwise
from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        components = [0]
        label = 0
        for prev, curr in pairwise(nums):
            if curr - prev > maxDiff:
                label += 1
            components.append(label)

        return [components[u] == components[v] for u, v in queries]
