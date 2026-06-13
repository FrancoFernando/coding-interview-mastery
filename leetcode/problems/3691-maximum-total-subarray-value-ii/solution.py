"""
LeetCode #3691: Maximum Total Subarray Value II
Difficulty: Hard
Link: https://leetcode.com/problems/maximum-total-subarray-value-ii/

Idea
----
Selecting k distinct subarrays to maximize the sum of their values
(max - min) is just "take the k subarrays with the largest value".

Key fact: a window that contains another window has a value >= the
inner one (a bigger window can only push max up and min down). So:
  - the whole array [0, n-1] has the global maximum value, and
  - shrinking a window can only keep the value the same or lower.

That lets us pull the top-k values out one at a time with a max-heap
(best-first search). Start from [0, n-1] and, when we pop a window,
push its slightly-smaller neighbors:
  - always push [l+1, r]   (shrink the left end)
  - push [l, r-1] only when l == 0   (shrink the right end)

The "l == 0" guard turns the lattice of windows into a tree where each
subarray has exactly one parent, so no subarray is ever pushed twice
and we need no visited set. Every parent strictly contains its child,
so values come out of the heap in non-increasing order.

A sparse table prices any window's max/min in O(1), so each heap step
is cheap regardless of how we reached the window.

Complexity
----------
Time:  O(n log n) to build the sparse tables + O(k log k) for the heap.
Space: O(n log n) for the two sparse tables.
"""
import heapq
from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def build(arr, func):  # func = max or min
            sp = [arr[:]]  # level 0: ranges of length 1
            j = 1
            while (1 << j) <= n:
                prev = sp[j - 1]
                half = 1 << (j - 1)  # each half-block has this length
                sp.append([func(prev[i], prev[i + half])
                           for i in range(n - (1 << j) + 1)])
                j += 1
            return sp

        def query(sp, l, r, func):
            j = (r - l + 1).bit_length() - 1  # largest 2^j fitting the range
            return func(sp[j][l], sp[j][r - (1 << j) + 1])

        spmax = build(nums, max)
        spmin = build(nums, min)

        def value(l, r):
            return query(spmax, l, r, max) - query(spmin, l, r, min)

        # Max-heap via negation (Python's heapq is a min-heap).
        heap = [(-value(0, n - 1), 0, n - 1)]
        total = 0
        for _ in range(k):
            v, l, r = heapq.heappop(heap)
            total += -v
            if l + 1 <= r:                       # shrink left: always
                heapq.heappush(heap, (-value(l + 1, r), l + 1, r))
            if l == 0 and r - 1 >= 0:            # shrink right: only on top row
                heapq.heappush(heap, (-value(0, r - 1), 0, r - 1))
        return total


def test_solution():
    sol = Solution()
    assert sol.maxTotalValue([1, 3, 2], 2) == 4
    assert sol.maxTotalValue([4, 2, 5, 1], 3) == 12
    print("All tests passed")


if __name__ == "__main__":
    test_solution()
