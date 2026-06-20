"""
LeetCode #1840: Maximum Building Height
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-building-height/
"""
from typing import List


class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        restrictions.sort(key=lambda x: x[0])

        for l, r in zip(restrictions, restrictions[1:]):
            (li, lh), (ri, rh) = l, r
            r[1] = min(rh, lh + (ri - li))

        for l, r in reversed(list(zip(restrictions, restrictions[1:]))):
            (li, lh), (ri, rh) = l, r
            l[1] = min(lh, rh + (ri - li))

        last_id, last_h = restrictions[-1]
        if last_id < n:
            restrictions.append([n, last_h + (n - last_id)])

        return max(((lh + rh + (ri - li)) // 2
                    for (li, lh), (ri, rh) in zip(restrictions, restrictions[1:])))


def test_solution():
    sol = Solution()

    assert sol.maxBuilding(5, [[2, 1], [4, 1]]) == 2
    print("Test 1 passed: n=5, [[2,1],[4,1]] -> 2")

    assert sol.maxBuilding(6, []) == 5
    print("Test 2 passed: n=6, [] -> 5")

    assert sol.maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]]) == 5
    print("Test 3 passed: n=10, [[5,3],[2,5],[7,4],[10,3]] -> 5")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
