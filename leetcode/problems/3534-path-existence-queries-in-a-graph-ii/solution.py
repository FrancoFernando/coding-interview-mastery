"""
LeetCode #3534: Path Existence Queries in a Graph II
Difficulty: Hard
Link: https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

Idea
----
An edge joins two nodes whose values differ by at most maxDiff. If we sort the
nodes by value, the neighbours of a node form a *contiguous* window of positions.
So the graph becomes a "jump game": from a sorted position you can step to any
position in an interval, and we want the minimum number of steps between two nodes.

- Connectivity: same as part I -- contiguous runs of sorted values whose
  consecutive gaps are <= maxDiff form one component. Different components => -1.
- Distance: greedily jump as far right as possible each step (optimal for a
  contiguous-interval jump game). To answer many queries fast, precompute those
  jumps in powers of two with binary lifting (a.k.a. binary jumping / sparse table).

Complexity: O((n + q) log n) time, O(n log n) space.
"""

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # 1. Sort nodes by value. `order[p]` = original index sitting at sorted position p.
        order = sorted(range(n), key=lambda i: nums[i])
        sorted_vals = [nums[i] for i in order]

        # Inverse map: original index -> its sorted position.
        pos = [0] * n
        for p, original in enumerate(order):
            pos[original] = p

        # 2. Component labels over sorted positions (contiguous runs, gap <= maxDiff).
        comp = [0] * n
        label = 0
        for p in range(1, n):
            if sorted_vals[p] - sorted_vals[p - 1] > maxDiff:
                label += 1
            comp[p] = label

        # 3. R[p] = farthest sorted position reachable from p in ONE jump.
        #    sorted_vals is non-decreasing, so the right boundary only moves right
        #    as p advances -> a single two-pointer pass, O(n).
        R = [0] * n
        r = 0
        for p in range(n):
            if r < p:
                r = p
            while r + 1 < n and sorted_vals[r + 1] - sorted_vals[p] <= maxDiff:
                r += 1
            R[p] = r

        # 4. Binary lifting: up[k][p] = farthest position reachable from p in 2^k jumps.
        LOG = max(1, n.bit_length())
        up = [[0] * n for _ in range(LOG)]
        up[0] = R
        for k in range(1, LOG):
            prev = up[k - 1]
            cur = up[k]
            for p in range(n):
                cur[p] = prev[prev[p]]  # 2^k jumps = two consecutive 2^(k-1) jumps

        # 5. Answer each query.
        def distance(a: int, b: int) -> int:
            # a, b are sorted positions in the SAME component, with a <= b.
            if a == b:
                return 0
            jumps = 0
            cur = a
            # Take the biggest power-of-two jumps that still fall short of b.
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    jumps += 1 << k
            # One final jump now lands on (or past) b.
            return jumps + 1

        answer = []
        for u, v in queries:
            a, b = pos[u], pos[v]
            if comp[a] != comp[b]:
                answer.append(-1)
            else:
                answer.append(distance(min(a, b), max(a, b)))
        return answer
