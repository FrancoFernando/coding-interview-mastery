"""
LeetCode #1189: Maximum Number of Balloons
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-number-of-balloons/
"""
import collections


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        available = collections.Counter(text)
        needed = collections.Counter("balloon")
        return min(available[char] // count for char, count in needed.items())


def test_solution():
    sol = Solution()
    assert sol.maxNumberOfBalloons("nlaebolko") == 1
    assert sol.maxNumberOfBalloons("loonbalxballpoon") == 2
    assert sol.maxNumberOfBalloons("leetcode") == 0
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
