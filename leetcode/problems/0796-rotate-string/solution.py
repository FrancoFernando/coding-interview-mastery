"""
LeetCode #796: Rotate string
Difficulty: Easy
Link: https://leetcode.com/problems/rotate-string/
"""

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        return goal in s+s if len(s) == len(goal) else False

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
