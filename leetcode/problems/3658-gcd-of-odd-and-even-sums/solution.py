"""
LeetCode #3658: GCD of Odd and Even Sums
Difficulty: Easy
Link: https://leetcode.com/problems/gcd-of-odd-and-even-sums/
"""
from math import gcd


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Sum of first n odd numbers = n^2; sum of first n even numbers = n(n+1).
        # gcd(n^2, n(n+1)) = n * gcd(n, n+1) = n, since consecutive integers are
        # coprime -- so the answer is simply n. Computed explicitly here for clarity.
        sum_odd = n * n
        sum_even = n * (n + 1)
        return gcd(sum_odd, sum_even)


def test_solution():
    sol = Solution()

    assert sol.gcdOfOddEvenSums(4) == 4
    print("Test 1 passed: n=4 -> 4")

    assert sol.gcdOfOddEvenSums(1) == 1
    print("Test 2 passed: n=1 -> 1")

    # The closed form is always n; spot-check a few.
    for n in range(1, 100):
        assert sol.gcdOfOddEvenSums(n) == n, n
    print("Test 3 passed: answer equals n for 1..99")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
