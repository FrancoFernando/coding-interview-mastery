"""
LeetCode #3286: Find a Safe Walk Through a Grid
Difficulty: Medium
Link: https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
"""
from typing import List
from collections import deque
from math import inf


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        # dist[cell] = minimum number of unsafe cells (grid == 1) stepped on to
        # reach that cell. Entering a cell costs grid[cell] (0 or 1), so edge
        # weights are 0/1 -> 0-1 BFS with a deque instead of a full heap.
        dist = {(0, 0): grid[0][0]}
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()
            # In 0-1 BFS a cell's distance is final when it is popped.
            if (r, c) == (rows - 1, cols - 1):
                return health - dist[(r, c)] > 0

            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    ndist = dist[(r, c)] + grid[nr][nc]
                    if dist.get((nr, nc), inf) > ndist:
                        dist[(nr, nc)] = ndist
                        if grid[nr][nc]:
                            q.append((nr, nc))       # cost 1 -> back
                        else:
                            q.appendleft((nr, nc))   # cost 0 -> front
        return False


def test_solution():
    sol = Solution()

    assert sol.findSafeWalk(
        [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]], 1
    ) is True
    print("Test 1 passed: health=1, safe path exists -> True")

    assert sol.findSafeWalk(
        [[0, 1, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1],
         [0, 0, 1, 0, 1, 0]], 3
    ) is False
    print("Test 2 passed: health=3 insufficient -> False")

    assert sol.findSafeWalk(
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]], 5
    ) is True
    print("Test 3 passed: health=5 through unsafe cells -> True")

    assert sol.findSafeWalk([[1]], 1) is False
    print("Test 4 passed: single unsafe cell, health=1 -> False")

    assert sol.findSafeWalk([[0]], 1) is True
    print("Test 5 passed: single safe cell -> True")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
