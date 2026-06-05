"""
LeetCode #3753: Total Waviness of Numbers in Range II
Difficulty: Hard
Link: https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/
"""

from functools import cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(num: int) -> int:
            digits = str(num)
            slots = len(digits)

            @cache
            def helper(pos, prev1, prev2, tight, started):
                if pos == slots:
                    return (1, 0)
                limit = int(digits[pos]) if tight else 9
                cnt, wav = 0, 0
                for d in range(limit + 1):
                    new_started = started or d > 0
                    new_prev1 = d if new_started else -1
                    new_tight = tight and d == limit
                    c, w = helper(pos + 1, new_prev1, prev1, new_tight, new_started)
                    extra_w = 0
                    if prev2 != -1:
                        if prev2 < prev1 > d or prev2 > prev1 < d:
                            extra_w = c
                    cnt += c
                    wav += w + extra_w
                return (cnt, wav)

            return helper(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)


def test_solution():
    sol = Solution()

    assert sol.totalWaviness(120, 130) == 3
    print("Test 1 passed: totalWaviness(120, 130) == 3")

    assert sol.totalWaviness(1, 99) == 0
    print("Test 2 passed: totalWaviness(1, 99) == 0 (no number has 3+ digits)")

    assert sol.totalWaviness(101, 109) == 9
    print("Test 3 passed: totalWaviness(101, 109) == 9 (all valleys)")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
