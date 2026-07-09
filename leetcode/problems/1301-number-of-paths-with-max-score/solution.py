"""
LeetCode #1301: Number of Paths with Max Score
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-paths-with-max-score/
"""
from typing import List
from math import inf


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        # score[i][j] = max digit sum on a path from S to (i, j); -inf = unreachable.
        # ways[i][j]  = number of paths achieving that max, mod 1e9+7.
        score = [[-inf for _ in range(n)] for _ in range(n)]
        ways = [[0 for _ in range(n)] for _ in range(n)]

        # S: contributes no digit, one way to start.
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        def combine_predecessors(i, j):
            # Moves are up / left / up-left, so a path reaches (i, j) FROM the
            # cells below / right / below-right. Iterating bottom-right -> top-left
            # guarantees those are already computed.
            best, cnt = -inf, 0
            for pi, pj in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                if pi < n and pj < n and score[pi][pj] >= 0:
                    if score[pi][pj] > best:          # strictly better -> replace
                        best, cnt = score[pi][pj], ways[pi][pj]
                    elif score[pi][pj] == best:       # tie -> add path counts
                        cnt = (cnt + ways[pi][pj]) % MOD
            return best, cnt

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if (i, j) == (n - 1, n - 1) or board[i][j] == 'X':
                    continue
                best, cnt = combine_predecessors(i, j)
                if best >= 0:  # reachable
                    val = 0 if board[i][j] == 'E' else int(board[i][j])
                    score[i][j] = best + val
                    ways[i][j] = cnt

        if score[0][0] < 0:  # E unreachable
            return [0, 0]
        return [score[0][0], ways[0][0] % MOD]


def test_solution():
    sol = Solution()

    assert sol.pathsWithMaxScore(["E23", "2X2", "12S"]) == [7, 1]
    print("Test 1 passed: ['E23','2X2','12S'] -> [7, 1]")

    assert sol.pathsWithMaxScore(["E12", "1X1", "21S"]) == [4, 2]
    print("Test 2 passed: ['E12','1X1','21S'] -> [4, 2]")

    assert sol.pathsWithMaxScore(["E11", "XXX", "11S"]) == [0, 0]
    print("Test 3 passed: disconnected by wall -> [0, 0]")

    assert sol.pathsWithMaxScore(["E1", "1S"]) == [1, 2]
    print("Test 4 passed: 2x2, two equal-score paths -> [1, 2]")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
