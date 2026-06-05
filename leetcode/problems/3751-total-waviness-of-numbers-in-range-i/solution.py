"""
LeetCode #3751: Total Waviness of Numbers in Range I
Difficulty: Medium
Link: https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
"""


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum(1
            for n in range(num1, num2 + 1)
            for s in (str(n),)
            for a, b, c in zip(s, s[1:], s[2:])
            if a < b > c or a > b < c)


def test_solution():
    sol = Solution()

    assert sol.totalWaviness(120, 130) == 3
    print("Test 1 passed: totalWaviness(120, 130) == 3")

    assert sol.totalWaviness(1, 99) == 0
    print("Test 2 passed: totalWaviness(1, 99) == 0 (no number has 3+ digits)")

    assert sol.totalWaviness(101, 109) == 9
    print("Test 3 passed: totalWaviness(101, 109) == 9 (all valleys)")

    assert sol.totalWaviness(1332, 1332) == 0
    print("Test 4 passed: totalWaviness(1332, 1332) == 0 (equal neighbors break peaks)")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
