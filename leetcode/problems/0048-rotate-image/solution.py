"""
LeetCode #48: Rotate image
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-image/
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n // 2):
            for i in range(layer, n-1-layer):
                tmp = matrix[layer][i] # save top
                matrix[layer][i] = matrix[n-1-i][layer] # left -> top
                matrix[n-1-i][layer] = matrix[n-1-layer][n-1-i]  # bottom -> left
                matrix[n-1-layer][n-1-i] = matrix[i][n-1-layer]  # right -> bottom
                matrix[i][n-1-layer] = tmp  # original top → right     

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
