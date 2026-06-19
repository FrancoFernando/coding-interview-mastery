"""
LeetCode #3838: Weighted Word Mapping
Difficulty: Easy
Link: https://leetcode.com/problems/weighted-word-mapping/
"""
from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        a, z = ord('a'), ord('z')
        return ''.join(chr(z - sum(weights[ord(c) - a] for c in word) % 26)
                       for word in words)


def test_solution():
    sol = Solution()
    w = list(range(1, 27))  # weights[i] = i + 1

    assert sol.mapWordWeights(["a"], w) == "y"
    print("Test 1 passed: 'a' -> weight 1 -> 'y'")

    assert sol.mapWordWeights(["z"], w) == "z"
    print("Test 2 passed: 'z' -> weight 26, 26 % 26 == 0 -> 'z'")

    assert sol.mapWordWeights(["ab", "yz"], w) == "wa"
    print("Test 3 passed: 'ab' (sum 3) -> 'w'; 'yz' (sum 51, %26=25) -> 'a'")

    assert sol.mapWordWeights(["zz"], w) == "z"
    print("Test 4 passed: 'zz' (sum 52, %26=0) -> 'z'")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
