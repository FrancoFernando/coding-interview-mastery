"""
LeetCode #154: Find Minimum in Rotated Sorted Array II
Difficulty: Medium
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[l]

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
