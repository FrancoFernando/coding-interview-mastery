"""
LeetCode #3614: Process String with Special Operations II
Difficulty: Hard
Link: https://leetcode.com/problems/process-string-with-special-operations-ii/
"""

class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Larger than any reachable k, and CAP // 2 > 10**15, so a capped
        # length always reports k as living in its first half (see README).
        CAP = 4 * 10**15

        # Forward pass: lengths[i] = length of result AFTER applying op s[i].
        lengths = []
        length = 0
        for c in s:
            if c == '*':
                length = max(length - 1, 0)
            elif c == '#':
                length = min(length * 2, CAP)
            elif c == '%':
                pass  # reversal does not change the length
            else:
                length += 1
            lengths.append(length)

        if k >= (lengths[-1] if lengths else 0):
            return '.'

        # Backward pass: map index k to the position it came from, op by op.
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            cur_len = lengths[i]  # length of the string k currently indexes into
            if c == '*':
                # Only the last char was removed; lower indices are unchanged.
                continue
            elif c == '#':
                half = cur_len // 2
                if k >= half:
                    k -= half  # k lived in the duplicated half
            elif c == '%':
                k = cur_len - 1 - k
            else:
                if k == cur_len - 1:
                    return c  # this append produced the character at k
                # otherwise k predates this append and is unchanged

        return '.'  # unreachable given the bounds check above


def test_solution():
    sol = Solution()
    assert sol.processStr("a#b%*", 1) == "a"
    assert sol.processStr("cd%#*#", 3) == "d"
    assert sol.processStr("z*#", 0) == "."
    print("All tests passed")

if __name__ == "__main__":
    test_solution()
