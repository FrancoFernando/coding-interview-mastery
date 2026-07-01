"""
LeetCode #2812: Find the Safest Path in a Grid
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-safest-path-in-a-grid/
"""
from typing import List
from collections import deque
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # ------------------------------------------------------------------
        # Phase 1: multi-source BFS -> dist[r][c] = Manhattan distance to the
        # nearest thief. Seed the queue with every thief at distance 0; BFS
        # expands in layers of increasing distance, so the first time a cell is
        # reached that layer IS its distance to the closest thief. On a
        # 4-directional grid, BFS step count equals Manhattan distance.
        # ------------------------------------------------------------------
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # ------------------------------------------------------------------
        # Phase 2: max-min path via Dijkstra with a max-heap. The safeness of a
        # path is the minimum dist over its cells; we want to maximize it.
        # best[r][c] = the largest achievable path-minimum to reach (r, c).
        # Always expand the reachable cell with the highest safeness so far,
        # carrying the running minimum. The first time we pop the destination,
        # its running minimum is the answer.
        # ------------------------------------------------------------------
        best = [[-1] * n for _ in range(n)]
        # Python's heapq is a min-heap; push negatives to pop the max first.
        heap = [(-dist[0][0], 0, 0)]
        best[0][0] = dist[0][0]

        while heap:
            neg_safe, r, c = heapq.heappop(heap)
            safe = -neg_safe
            if (r, c) == (n - 1, n - 1):
                return safe
            if safe < best[r][c]:
                continue  # a better path to this cell was already settled
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # safeness of extending the path into (nr, nc)
                    cand = min(safe, dist[nr][nc])
                    if cand > best[nr][nc]:
                        best[nr][nc] = cand
                        heapq.heappush(heap, (-cand, nr, nc))

        return best[n - 1][n - 1]


def test_solution():
    sol = Solution()

    assert sol.maximumSafenessFactor([[1, 0, 0], [0, 0, 0], [0, 0, 1]]) == 0
    print("Test 1 passed: thieves at both corners -> 0")

    assert sol.maximumSafenessFactor(
        [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    ) == 2
    print("Test 2 passed: single thief -> 2")

    assert sol.maximumSafenessFactor(
        [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
    ) == 2
    print("Test 3 passed: two thieves -> 2")

    assert sol.maximumSafenessFactor([[0, 1], [0, 0]]) == 1
    print("Test 4 passed: 2x2 -> 1")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
