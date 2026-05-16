"""
LeetCode #153: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()

'''
left comparison
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l+r) // 2
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
'''
