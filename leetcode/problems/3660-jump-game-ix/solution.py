"""
LeetCode #3660: Jump Game IX
Difficulty: Medium
Link: https://leetcode.com/problems/jump-game-ix/
"""

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_max = [-1] * n
        prefix_max[0] = nums[0]
        for i in range(1,n):
            prefix_max[i] = (max(nums[i], prefix_max[i-1]))

        suffix_min = [-1] * n
        suffix_min[-1] = nums[-1]
        for i in reversed(range(n-1)):
            suffix_min[i] = min(nums[i], suffix_min[i+1])
        
        answer = [0] * n
        segment_start = 0
        for i in range(n-1):
            if prefix_max[i] <= suffix_min[i+1]:
                answer[segment_start:i+1] = [prefix_max[i]] * (i-segment_start+1)
                segment_start = i+1

        answer[segment_start:] = [prefix_max[-1]] * (n-segment_start)
        return answer

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()

# more compact solution with itertools and handling last segment in the loop 
from itertools import accumulate
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_max = list(accumulate(nums,max))
        suffix_min = list(accumulate(reversed(nums),min))[::-1]
        
        answer = []
        segment_start = 0
        for i in range(n):
            if i == n-1 or prefix_max[i] <= suffix_min[i+1]:
                answer.extend([prefix_max[i]] * (i-segment_start+1))
                segment_start = i+1

        return answer
