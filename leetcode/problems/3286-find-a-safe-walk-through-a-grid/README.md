# 3286. Find a Safe Walk Through a Grid

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/find-a-safe-walk-through-a-grid/)

## Problem Description

From `(0,0)` to `(m-1,n-1)` on a binary grid, each unsafe cell (`grid = 1`) costs 1 health. Return `true` if you can reach the end with health ≥ 1.

## Approach

Health lost along a path = number of unsafe cells stepped on. So you survive iff:

```
health - (min unsafe cells on any path) >= 1
```

Reduce the yes/no question to a **minimum-cost path**: minimize the unsafe cells crossed, then compare to `health`.

Model it as a grid graph where entering a cell costs `grid[cell]` — either **0** (safe) or **1** (unsafe). Because every edge weight is 0 or 1, use **0-1 BFS** with a deque instead of a full Dijkstra heap:

- Track `dist[cell]` = min unsafe cells to reach it (unseen = `inf`).
- Relax a neighbor only on strict improvement: `ndist = dist[cur] + grid[neighbor]`.
- Push the neighbor to the **front** on a 0-cost move, the **back** on a 1-cost move. This keeps the deque in non-decreasing cost order, O(1) per operation.

A cell's distance is final when it is **popped** (not when discovered), so the destination check sits at pop time.

## Complexity

- **Time:** O(m · n) — each cell is settled once; deque ops are O(1).
- **Space:** O(m · n) for `dist` and the deque.

## Notes

- **Seed the start with `grid[0][0]`**, not 0 — the first cell may itself be unsafe.
- The trailing `return False` is unreachable here: you may pass through any cell, so the whole grid is connected and the destination is always eventually popped. Kept as a defensive fallback.
- Using `dist.get(cell, inf)` (or a 2D array of `inf`) collapses the "unseen or improvable" guard into a single comparison. Prefer `dict.get` over `defaultdict` here, since a `defaultdict` read would insert phantom keys.
- Edge weights are only 0/1, so 0-1 BFS beats a min-heap Dijkstra (O(mn) vs O(mn log(mn))). A max-min variant of the same grid appears in [2812](../2812-find-the-safest-path-in-a-grid).
