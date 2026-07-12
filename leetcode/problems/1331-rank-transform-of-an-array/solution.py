"""
LeetCode #1331: Rank Transform of an Array
Difficulty: Easy
Link: https://leetcode.com/problems/rank-transform-of-an-array/
"""
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # A value's rank is its 1-based position among the distinct sorted values:
        # dedup + sort handles "equal -> same rank" and "no gaps" automatically.
        unique_sorted = sorted(set(arr))
        num_to_rank = {val: idx + 1 for idx, val in enumerate(unique_sorted)}
        return [num_to_rank[n] for n in arr]


def test_solution():
    sol = Solution()

    assert sol.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]
    print("Test 1 passed: [40,10,20,30] -> [4,1,2,3]")

    assert sol.arrayRankTransform([100, 100, 100]) == [1, 1, 1]
    print("Test 2 passed: equal elements share rank -> [1,1,1]")

    assert sol.arrayRankTransform(
        [37, 12, 28, 9, 100, 56, 80, 5, 12]
    ) == [5, 3, 4, 2, 8, 6, 7, 1, 3]
    print("Test 3 passed: duplicates keep same rank")

    assert sol.arrayRankTransform([]) == []
    print("Test 4 passed: empty array -> []")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
