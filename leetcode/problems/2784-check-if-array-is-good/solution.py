"""
LeetCode #2784: Check if Array is Good
Difficulty: Medium
Link: https://leetcode.com/problems/check-if-array-is-good/
"""

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1 # 1,...,n 
        frequency = Counter(nums)
        return frequency[n] == 2 and all(frequency[i] == 1 for i in range(1,n))

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
