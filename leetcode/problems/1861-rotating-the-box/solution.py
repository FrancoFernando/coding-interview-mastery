"""
LeetCode #1861: Rotating the Box
Difficulty: Medium
Link: https://leetcode.com/problems/rotating-the-box/
"""

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        outputGrid = [[] for _ in range(len(boxGrid[0]))]
        for row in boxGrid:
            empty = -1
            for i in reversed(range(len(row))):
                if row[i] == "." and empty < 0:
                    empty = i
                if row[i] == "#" and empty >= 0: 
                   row[empty] = "#"
                   row[i] = "."
                   empty -= 1
                if row[i] == "*":
                     empty = -1
        
        for j in reversed(range(len(boxGrid))):
            for i in range(len(boxGrid[0])):
                outputGrid[i].append(boxGrid[j][i])

        return boxGrid              

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
