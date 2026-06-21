"""
LeetCode #1833: Maximum Ice Cream Bars
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-ice-cream-bars/
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        freq = [0] * (max_cost + 1)
        for c in costs:
            freq[c] += 1

        bought = 0
        for cost in range(1, max_cost + 1):
            if coins < cost:
                break
            buyable = min(freq[cost], coins // cost)
            bought += buyable
            coins -= buyable * cost

        return bought


def test_solution():
    sol = Solution()

    assert sol.maxIceCream([1, 3, 2, 4, 1], 7) == 4
    print("Test 1 passed: costs=[1,3,2,4,1], coins=7 -> 4")

    assert sol.maxIceCream([10, 6, 8, 7, 7, 8], 5) == 0
    print("Test 2 passed: cheapest item costs more than coins -> 0")

    assert sol.maxIceCream([1, 6, 3, 1, 2, 5], 20) == 6
    print("Test 3 passed: enough coins to buy everything -> 6")

    assert sol.maxIceCream([5, 5, 5, 5], 10) == 2
    print("Test 4 passed: bulk buy of same cost -> 2")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
