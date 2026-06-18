"""
LeetCode #3612: Process String with Special Operations I
Difficulty: Medium
Link: https://leetcode.com/problems/process-string-with-special-operations-i/
"""


class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.islower():
                result.append(c)
            elif c == "*" and result:
                result.pop()
            elif c == "#":
                result *= 2
            elif c == "%":
                result.reverse()
        return ''.join(result)


def test_solution():
    sol = Solution()

    assert sol.processStr("a#b%*") == "ba"
    print("Test 1 passed: processStr('a#b%*') == 'ba'")

    assert sol.processStr("*") == ""
    print("Test 2 passed: '*' on empty result is a no-op")

    assert sol.processStr("abc") == "abc"
    print("Test 3 passed: plain letters append")

    assert sol.processStr("ab#") == "abab"
    print("Test 4 passed: '#' duplicates")

    assert sol.processStr("ab%") == "ba"
    print("Test 5 passed: '%' reverses")

    assert sol.processStr("a##") == "aaaa"
    print("Test 6 passed: consecutive '#' compound")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
