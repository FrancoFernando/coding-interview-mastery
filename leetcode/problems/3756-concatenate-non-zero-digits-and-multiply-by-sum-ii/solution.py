"""
LeetCode #3756: Concatenate Non-Zero Digits and Multiply by Sum II
Difficulty: Medium
Link: https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
"""
from typing import List


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)

        # Prefix arrays over s[0..i-1]:
        #   P[i] = number formed by concatenating its non-zero digits, mod p
        #   C[i] = count of non-zero digits
        #   D[i] = sum of all digits (zeros add 0, so this is the non-zero sum too)
        P = [0] * (m + 1)
        C = [0] * (m + 1)
        D = [0] * (m + 1)
        for i, ch in enumerate(s):
            d = ord(ch) - 48
            D[i + 1] = D[i] + d
            if d:
                P[i + 1] = (P[i] * 10 + d) % MOD
                C[i + 1] = C[i] + 1
            else:
                P[i + 1] = P[i]
                C[i + 1] = C[i]

        # pow10[k] = 10^k mod p, k up to the max possible non-zero count.
        pow10 = [1] * (m + 1)
        for k in range(1, m + 1):
            pow10[k] = pow10[k - 1] * 10 % MOD

        # For a range [l, r], the non-zero digits of s[0..r] split into the
        # prefix block P[l] (digits before l) followed by the range block X:
        #   P[r+1] = P[l] * 10^k + X,  k = non-zero digits in range
        # => X = P[r+1] - P[l] * 10^k (mod p). Subtraction, so no modular inverse.
        ans = []
        for l, r in queries:
            k = C[r + 1] - C[l]
            x = (P[r + 1] - P[l] * pow10[k]) % MOD   # % keeps it non-negative
            digit_sum = D[r + 1] - D[l]
            ans.append(x * digit_sum % MOD)
        return ans


def _brute(s, queries):
    MOD = 10**9 + 7
    out = []
    for l, r in queries:
        nz = [c for c in s[l:r + 1] if c != '0']
        x = int(''.join(nz)) if nz else 0
        out.append(x * sum(int(c) for c in nz) % MOD)
    return out


def test_solution():
    sol = Solution()

    assert sol.sumAndMultiply("10203004", [[0, 7]]) == [12340]
    print("Test 1 passed: full string -> [12340]")

    assert sol.sumAndMultiply("10203004", [[2, 5]]) == [115]
    print("Test 2 passed: substring '2030' -> [115]")

    assert sol.sumAndMultiply("000", [[0, 2]]) == [0]
    print("Test 3 passed: all zeros -> [0]")

    # Randomized cross-check against brute force.
    import random
    rng = random.Random(0)
    for _ in range(2000):
        length = rng.randint(1, 12)
        s = ''.join(rng.choice("0123456789") for _ in range(length))
        qs = [sorted((rng.randrange(length), rng.randrange(length)))
              for _ in range(rng.randint(1, 5))]
        qs = [[a, b] for a, b in qs]
        assert sol.sumAndMultiply(s, qs) == _brute(s, qs), (s, qs)
    print("Test 4 passed: matches brute force on 2000 random cases")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
