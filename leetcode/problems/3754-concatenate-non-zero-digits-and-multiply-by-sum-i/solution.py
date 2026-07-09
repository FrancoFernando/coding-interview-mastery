"""
LeetCode #3754: Concatenate Non-Zero Digits and Multiply by Sum I
Difficulty: Easy
Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/
"""


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Peel digits right-to-left. digit_sum takes every digit (zeros add 0);
        # new_x rebuilds the number from only the non-zero digits, so `mult`
        # advances only when a non-zero digit is placed -> the zeros vanish
        # with no gaps.
        digit_sum = 0
        new_x = 0
        mult = 1
        while n > 0:
            n, d = divmod(n, 10)
            digit_sum += d
            if d:
                new_x += d * mult
                mult *= 10
        return new_x * digit_sum


def test_solution():
    sol = Solution()

    assert sol.sumAndMultiply(10203004) == 12340
    print("Test 1 passed: 10203004 -> 12340")

    assert sol.sumAndMultiply(0) == 0
    print("Test 2 passed: 0 -> 0")

    assert sol.sumAndMultiply(1234) == 1234 * 10
    print("Test 3 passed: no zeros -> 12340")

    assert sol.sumAndMultiply(5) == 25
    print("Test 4 passed: single digit -> 5 * 5 = 25")

    assert sol.sumAndMultiply(1000) == 1
    print("Test 5 passed: 1000 -> x=1, sum=1 -> 1")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
