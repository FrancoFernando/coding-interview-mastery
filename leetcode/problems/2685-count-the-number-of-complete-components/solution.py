"""
LeetCode #2685: Count the Number of Complete Components
Difficulty: Medium
Link: https://leetcode.com/problems/count-the-number-of-complete-components/
"""
from typing import List
from collections import deque


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def collect_component(start: int) -> List[int]:
            """Return all nodes reachable from `start`, marking them visited."""
            nodes = []
            q = deque([start])
            visited[start] = True
            while q:
                curr = q.popleft()
                nodes.append(curr)
                for adj in graph[curr]:
                    if not visited[adj]:
                        visited[adj] = True
                        q.append(adj)
            return nodes

        # A component of k vertices is complete iff every vertex is joined to all
        # k-1 others, i.e. every vertex has degree k-1.
        result = 0
        for node in range(n):
            if not visited[node]:
                nodes = collect_component(node)
                k = len(nodes)
                if all(len(graph[v]) == k - 1 for v in nodes):
                    result += 1
        return result


def test_solution():
    sol = Solution()

    assert sol.countCompleteComponents(
        6, [[0, 1], [0, 2], [1, 2], [3, 4]]
    ) == 3
    print("Test 1 passed: triangle + edge + singleton -> 3")

    assert sol.countCompleteComponents(
        6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    ) == 1
    print("Test 2 passed: only the triangle is complete -> 1")

    assert sol.countCompleteComponents(3, []) == 3
    print("Test 3 passed: three isolated vertices -> 3")

    assert sol.countCompleteComponents(4, [[0, 1], [1, 2], [2, 3], [3, 0]]) == 0
    print("Test 4 passed: 4-cycle (missing diagonals) -> 0")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
