"""
LeetCode #1288: Remove Covered Intervals
Difficulty: Medium
Link: https://leetcode.com/problems/remove-covered-intervals/
"""
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start ascending so every potential coverer is seen first; break
        # ties by end descending so the longer of two same-start intervals leads
        # and correctly covers the shorter one. Then an interval survives iff it
        # ends farther right than everything before it (end > max_end).
        cnt = 0
        max_end = -1
        for start, end in sorted(intervals, key=lambda i: (i[0], -i[1])):
            if end > max_end:
                cnt += 1
                max_end = end
        return cnt


def test_solution():
    sol = Solution()

    assert sol.removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]) == 2
    print("Test 1 passed: [[1,4],[3,6],[2,8]] -> 2")

    assert sol.removeCoveredIntervals([[1, 4], [2, 3]]) == 1
    print("Test 2 passed: [[1,4],[2,3]] -> 1")

    # Same start: [1,6] covers [1,4]; tie-break (end desc) is what catches it.
    assert sol.removeCoveredIntervals([[1, 4], [1, 6]]) == 1
    print("Test 3 passed: same-start cover -> 1")

    assert sol.removeCoveredIntervals([[1, 2], [3, 4], [5, 6]]) == 3
    print("Test 4 passed: disjoint intervals -> 3")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
