"""
LeetCode #1358: Number of Substrings Containing All Three Characters
Difficulty: Medium
Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # Count valid substrings by their right endpoint r. A substring ending at
        # r is valid iff its start is <= the last-seen index of every character,
        # i.e. start <= min(last_seen). That gives min(last_seen) + 1 valid starts.
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        result = 0
        for r in range(len(s)):
            last_seen[s[r]] = r
            earliest = min(last_seen.values())
            if earliest != -1:  # -1 only while some character hasn't appeared yet
                result += 1 + earliest
        return result


def test_solution():
    sol = Solution()

    assert sol.numberOfSubstrings("abcabc") == 10
    print("Test 1 passed: 'abcabc' -> 10")

    assert sol.numberOfSubstrings("aaacb") == 3
    print("Test 2 passed: 'aaacb' -> 3")

    assert sol.numberOfSubstrings("abc") == 1
    print("Test 3 passed: 'abc' -> 1")

    assert sol.numberOfSubstrings("aaa") == 0
    print("Test 4 passed: no b/c -> 0")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
