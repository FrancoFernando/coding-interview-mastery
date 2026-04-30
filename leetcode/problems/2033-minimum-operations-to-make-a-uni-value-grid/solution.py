"""
LeetCode #2033: Minimum Operations to Make a Uni-Value Grid
Difficulty: Medium
Link: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
"""

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        flattened = []
        remainder = grid[0][0] % x
        for row in grid:
            for num in row:
                if (num % x) != remainder:
                    return -1
                flattened.append(num)

        flattened.sort()
        middle = flattened[len(flattened) // 2]

        return sum((abs(middle - num) // x) for row in grid for num in row)

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
