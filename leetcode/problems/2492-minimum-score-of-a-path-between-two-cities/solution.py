"""
LeetCode #2492: Minimum Score of a Path Between Two Cities
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
"""
from typing import List
from collections import deque
from math import inf


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Paths may reuse roads and revisit cities, so any edge in city 1's
        # connected component can be dragged onto a 1 -> n path. The score is the
        # minimum edge on the path, so the answer is simply the smallest edge
        # weight in that component (n is guaranteed to be in it).
        graph = [[] for _ in range(n + 1)]
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        visited = {1}
        q = deque([1])
        min_score = inf

        while q:
            node = q.popleft()
            for adj, dist in graph[node]:
                # Update on every incident edge -- the cheapest one may connect
                # two already-visited nodes.
                min_score = min(min_score, dist)
                if adj not in visited:
                    visited.add(adj)
                    q.append(adj)
        return min_score


def test_solution():
    sol = Solution()

    assert sol.minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]) == 5
    print("Test 1 passed: -> 5")

    assert sol.minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]) == 2
    print("Test 2 passed: -> 2")

    # Cheapest edge sits between two nodes both reached before it is examined.
    assert sol.minScore(3, [[1, 2, 5], [1, 3, 4], [2, 3, 1]]) == 1
    print("Test 3 passed: min edge between two visited nodes -> 1")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
