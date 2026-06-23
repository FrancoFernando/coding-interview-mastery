"""
LeetCode #3699: Number of ZigZag Arrays I
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-zigzag-arrays-i/
"""


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # i = 2 base case: any length-2 array is a valid zigzag.
        up = [(v - 1) % MOD for v in range(1, m + 1)]   # last step went up, ending at v
        down = [(m - v) % MOD for v in range(1, m + 1)]  # last step went down, ending at v

        for _ in range(3, n + 1):
            # up[v]   = sum of down over u < v   -> prefix sums of `down`
            # down[v] = sum of up   over u > v   -> suffix sums of `up`
            pre = [0] * (m + 1)
            for i in range(m):
                pre[i + 1] = (pre[i] + down[i]) % MOD
            suf = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suf[i] = (suf[i + 1] + up[i]) % MOD

            up = [pre[v] for v in range(m)]
            down = [suf[v + 1] for v in range(m)]

        return sum(up + down) % MOD


def test_solution():
    sol = Solution()

    assert sol.zigZagArrays(3, 4, 5) == 2
    print("Test 1 passed: n=3, [4,5] -> 2")

    assert sol.zigZagArrays(3, 1, 3) == 10
    print("Test 2 passed: n=3, [1,3] -> 10")

    # m = 2: only the two strictly alternating arrays of any length.
    assert sol.zigZagArrays(4, 1, 2) == 2
    print("Test 3 passed: n=4, [2 values] -> 2")

    # Sanity vs. brute force on small inputs.
    from itertools import product

    def brute(n, l, r):
        count = 0
        for arr in product(range(l, r + 1), repeat=n):
            ok = True
            for i in range(1, n):
                if arr[i] == arr[i - 1]:
                    ok = False
                    break
            for i in range(2, n):
                a, b, c = arr[i - 2], arr[i - 1], arr[i]
                if (a < b < c) or (a > b > c):
                    ok = False
                    break
            count += ok
        return count % (10**9 + 7)

    for n in range(3, 7):
        for l, r in [(1, 3), (2, 5), (1, 4)]:
            assert sol.zigZagArrays(n, l, r) == brute(n, l, r), (n, l, r)
    print("Test 4 passed: matches brute force across small inputs")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
