"""
LeetCode #3633: Earliest Finish Time for Land and Water Rides I
Difficulty: Medium
Link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/
"""

from itertools import product
from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        landFinish = [s + d for s, d in zip(landStartTime, landDuration)]
        waterFinish = [s + d for s, d in zip(waterStartTime, waterDuration)]

        return min(
            min(
                max(land_finish, water_start) + water_duration,
                max(water_finish, land_start) + land_duration,
            )
            for (land_start, land_duration, land_finish), \
                (water_start, water_duration, water_finish) in product(
                    zip(landStartTime, landDuration, landFinish),
                    zip(waterStartTime, waterDuration, waterFinish),
                )
        )


def test_solution():
    sol = Solution()

    assert sol.earliestFinishTime([2, 8], [4, 1], [6], [3]) == 9
    print("Test 1 passed: simple two-land one-water case == 9")

    # Single ride each, second already open when first finishes.
    assert sol.earliestFinishTime([0], [5], [0], [5]) == 10
    print("Test 2 passed: back-to-back, no waiting == 10")

    # Water opens late: doing water first forces a wait.
    assert sol.earliestFinishTime([0], [2], [100], [1]) == 101
    print("Test 3 passed: land first beats waiting for late water == 101")

    # Multiple options: the min-finish land ride wins.
    assert sol.earliestFinishTime([1, 5], [2, 1], [10], [2]) == 12
    print("Test 4 passed: best pairing chosen == 12")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
