"""
LeetCode #396: Rotate Function
Difficulty: Medium
Link: https://leetcode.com/problems/rotate-function/
"""

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        n = len(nums)
        total_sum = sum(nums)
        current_F = max_F = sum(num*c for c, num in enumerate(nums))

        for k in range(1,n):
            current_F = current_F + total_sum - (n * nums[n-k])
            max_F = max(max_F,current_F)
        return max_F

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
