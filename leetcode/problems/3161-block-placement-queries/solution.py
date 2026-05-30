from sortedcontainers import SortedList
from typing import List


class SegmentTree:
    """Range-max + point-update segment tree."""

    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (4 * n)

    def update(self, pos: int, value: int) -> None:
        self._update(1, 0, self.n - 1, pos, value)

    def query(self, lo: int, hi: int) -> int:
        if lo > hi:
            return 0
        return self._query(1, 0, self.n - 1, lo, hi)

    def _update(self, node, node_lo, node_hi, pos, value):
        if node_lo == node_hi:
            self.tree[node] = value
            return
        mid = (node_lo + node_hi) // 2
        if pos <= mid:
            self._update(2 * node, node_lo, mid, pos, value)
        else:
            self._update(2 * node + 1, mid + 1, node_hi, pos, value)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def _query(self, node, node_lo, node_hi, lo, hi):
        if hi < node_lo or node_hi < lo:
            return 0
        if lo <= node_lo and node_hi <= hi:
            return self.tree[node]
        mid = (node_lo + node_hi) // 2
        return max(
            self._query(2 * node, node_lo, mid, lo, hi),
            self._query(2 * node + 1, mid + 1, node_hi, lo, hi),
        )


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        MAX_X = 50_001
        st = SegmentTree(MAX_X)
        obstacles = SortedList([0])
        results: List[bool] = []

        for q in queries:
            if q[0] == 1:
                p = q[1]
                i = obstacles.bisect_left(p)
                prev = obstacles[i - 1]
                st.update(p, p - prev)
                if i < len(obstacles):
                    nxt = obstacles[i]
                    st.update(nxt, nxt - p)
                obstacles.add(p)
            else:
                _, x, sz = q
                i = obstacles.bisect_right(x) - 1
                last = obstacles[i]
                tail = x - last
                best_inside = st.query(0, last)
                results.append(max(best_inside, tail) >= sz)

        return results
