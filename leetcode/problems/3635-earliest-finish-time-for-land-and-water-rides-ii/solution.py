"""
LeetCode #3635: Earliest Finish Time for Land and Water Rides II
Difficulty: Medium
Link: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/
"""

from typing import List


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        def best(first_start, first_dur, second_start, second_dur):
            first_finish = min(s + d for s, d in zip(first_start, first_dur))
            return min(max(first_finish, s) + d for s, d in zip(second_start, second_dur))

        return min(
            best(landStartTime, landDuration, waterStartTime, waterDuration),
            best(waterStartTime, waterDuration, landStartTime, landDuration),
        )


def test_solution():
    sol = Solution()

    assert sol.earliestFinishTime([2, 8], [4, 1], [6], [3]) == 9
    print("Test 1 passed: simple two-land one-water case == 9")

    assert sol.earliestFinishTime([0], [5], [0], [5]) == 10
    print("Test 2 passed: back-to-back, no waiting == 10")

    assert sol.earliestFinishTime([0], [2], [100], [1]) == 101
    print("Test 3 passed: land first beats waiting for late water == 101")

    assert sol.earliestFinishTime([1, 5], [2, 1], [10], [2]) == 12
    print("Test 4 passed: best pairing chosen == 12")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
