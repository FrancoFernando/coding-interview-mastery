"""
LeetCode #3700: Number of ZigZag Arrays II
Difficulty: Hard
Link: https://leetcode.com/problems/number-of-zigzag-arrays-ii/
"""


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Same recurrence as Part I, but n can be 1e9 while m <= 75.
        #
        # State (symmetry-reduced): up[v] = # zigzags ending at value v (1..m)
        # whose last step went up. By value-reversal symmetry,
        #   down[v] = up[m + 1 - v],
        # so the `up` vector alone is sufficient state.
        #
        # One step is a fixed linear map new_up = A @ up:
        #   new_up[v] = sum_{u<v} down[u] = sum_{u<v} up[m+1-u] = sum_{j >= m+2-v} up[j]
        # so (1-indexed) A[v][j] = 1  iff  v + j >= m + 2.
        # 0-indexed (i = v-1, k = j-1): A[i][k] = 1  iff  i + k >= m.
        A = [[1 if i + k >= m else 0 for k in range(m)] for i in range(m)]

        def mat_mult(X, Y):
            rows, inner, cols = len(X), len(Y), len(Y[0])
            res = [[0] * cols for _ in range(rows)]
            for i in range(rows):
                Xi, Ri = X[i], res[i]
                for k in range(inner):
                    a = Xi[k]
                    if a:
                        Yk = Y[k]
                        for j in range(cols):
                            Ri[j] = (Ri[j] + a * Yk[j]) % MOD
            return res

        def mat_pow(M, e):
            size = len(M)
            R = [[1 if i == j else 0 for j in range(size)] for i in range(size)]  # identity
            while e:
                if e & 1:
                    R = mat_mult(R, M)
                M = mat_mult(M, M)
                e >>= 1
            return R

        # Base vector at length 2: up[v] = v - 1. Advance to length n: A^(n-2).
        An = mat_pow(A, n - 2)
        base = [v - 1 for v in range(1, m + 1)]
        up_n = [sum(An[i][k] * base[k] for k in range(m)) % MOD for i in range(m)]

        # answer = sum_v (up[n][v] + down[n][v]) = 2 * sum_v up[n][v]
        return (2 * sum(up_n)) % MOD


def test_solution():
    sol = Solution()

    assert sol.zigZagArrays(3, 4, 5) == 2
    print("Test 1 passed: n=3, [4,5] -> 2")

    assert sol.zigZagArrays(3, 1, 3) == 10
    print("Test 2 passed: n=3, [1,3] -> 10")

    # m = 2: only the two strictly alternating arrays of any length.
    assert sol.zigZagArrays(4, 1, 2) == 2
    print("Test 3 passed: n=4, [2 values] -> 2")

    # Brute force on tiny inputs.
    from itertools import product

    def brute(n, l, r):
        count = 0
        for arr in product(range(l, r + 1), repeat=n):
            ok = all(arr[i] != arr[i - 1] for i in range(1, n))
            if ok:
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

    # Cross-check against the O(n*m) Part I DP for moderate n (where it is still cheap).
    def linear_dp(n, l, r):
        MOD = 10**9 + 7
        m = r - l + 1
        up = [(v - 1) % MOD for v in range(1, m + 1)]
        down = [(m - v) % MOD for v in range(1, m + 1)]
        for _ in range(3, n + 1):
            pre = [0] * (m + 1)
            for i in range(m):
                pre[i + 1] = (pre[i] + down[i]) % MOD
            suf = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suf[i] = (suf[i + 1] + up[i]) % MOD
            up = [pre[v] for v in range(m)]
            down = [suf[v + 1] for v in range(m)]
        return sum(up + down) % MOD

    for n in [10, 50, 200, 1000]:
        for l, r in [(1, 5), (3, 20), (1, 40)]:
            assert sol.zigZagArrays(n, l, r) == linear_dp(n, l, r), (n, l, r)
    print("Test 5 passed: matches O(n*m) DP for moderate n")

    # Large n with max m must still finish fast (matrix exponentiation).
    big = sol.zigZagArrays(10**9, 1, 75)
    assert 0 <= big < 10**9 + 7
    print(f"Test 6 passed: n=1e9, m=75 -> {big} (ran in O(m^3 log n))")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
