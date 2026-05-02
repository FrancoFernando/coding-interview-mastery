"""
LeetCode #788: Rotated Digits
Difficulty: Medium
Link: https://leetcode.com/problems/rotated-digits/
"""

class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        changing = {'2', '5', '6', '9'}
        invalid = {'3', '4', '7'}
        result = 0

        for i in range(1,n+1):
            num = str(i)
            changed = False
            can_be_rotated = True
            for digit in num:
                if digit in invalid:
                    can_be_rotated = False
                    break
                if digit in changing:
                    changed = True
            if changed and can_be_rotated:
                result += 1
        return result

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
