"""
LeetCode #3742: Maximum Path Score in a Grid
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-path-score-in-a-grid/
"""

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        NEG_INF = float('-inf')
        dp = [[[NEG_INF] * (k + 1) for _ in range(n)] for _ in range(m)]

        dp[0][0][1 if grid[0][0] > 0 else 0] = grid[0][0]

        def get(i, j, c):
            if i < 0 or j < 0 or c < 0:
                return NEG_INF
            return dp[i][j][c]   # which is -inf if never set

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                score = grid[i][j]
                cost = 1 if grid[i][j] > 0 else 0 
                for c in range(k+1):
                    dp[i][j][c] = score + max(get(i-1, j, c-cost), get(i, j-1, c-cost))

        result = max([dp[m-1][n-1][c] for c in range(k+1)])

        return -1 if result == NEG_INF else result


def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
