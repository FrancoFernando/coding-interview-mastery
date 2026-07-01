"""
LeetCode #1967: Number of Strings That Appear as Substrings in Word
Difficulty: Easy
Link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
"""
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # `pattern in word` is Python's built-in substring test; count the hits.
        return sum(1 for pattern in patterns if pattern in word)


def test_solution():
    sol = Solution()

    assert sol.numOfStrings(["a", "abc", "bc", "d"], "abc") == 3
    print("Test 1 passed: 3 of 4 patterns are substrings")

    assert sol.numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2
    print("Test 2 passed: only 'a' and 'b' present -> 2")

    assert sol.numOfStrings(["abc", "cba"], "xyz") == 0
    print("Test 3 passed: none present -> 0")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
