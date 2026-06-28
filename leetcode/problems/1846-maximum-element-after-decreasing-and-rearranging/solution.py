"""
LeetCode #1846: Maximum Element After Decreasing and Rearranging
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
"""
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Build the steepest legal staircase: sort ascending, then let each value
        # climb at most one step above the previous one. min() enforces both rules:
        #   prev + 1 -> adjacent difference can be at most 1
        #   num      -> we may only decrease a value, never raise it
        # prev starts at 0 so the first element is forced to min(1, num) = 1.
        prev = 0
        for num in sorted(arr):
            prev = min(prev + 1, num)
        return prev


def test_solution():
    sol = Solution()
    f = sol.maximumElementAfterDecrementingAndRearranging

    assert f([2, 2, 1, 2, 1]) == 2
    print("Test 1 passed: [2,2,1,2,1] -> 2")

    assert f([100, 1, 1000]) == 3
    print("Test 2 passed: [100,1,1000] -> 3")

    assert f([1, 2, 3, 4, 5]) == 5
    print("Test 3 passed: already valid -> 5")

    assert f([1]) == 1
    print("Test 4 passed: single element -> 1")

    assert f([1000000000]) == 1
    print("Test 5 passed: single large element forced to 1")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
