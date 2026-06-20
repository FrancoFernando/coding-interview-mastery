"""
LeetCode #1732: Find the Highest Altitude
Difficulty: Easy
Link: https://leetcode.com/problems/find-the-highest-altitude/
"""
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        result = 0
        altitude = 0

        for num in gain:
            altitude += num
            result = max(result, altitude)

        return result

    # One-liner with itertools.accumulate (running prefix sums); start at 0:
    # from itertools import accumulate
    # return max(0, max(accumulate(gain)))

def test_solution():
    sol = Solution()
    assert sol.largestAltitude([-5, 1, 5, 0, -7]) == 1
    assert sol.largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
