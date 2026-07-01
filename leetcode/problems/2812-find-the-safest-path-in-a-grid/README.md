# 2812. Find the Safest Path in a Grid

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/find-the-safest-path-in-a-grid/)

## Problem Description

Given an `n x n` grid where `1` marks a thief and `0` an empty cell, the **safeness factor** of a path from `(0,0)` to `(n-1,n-1)` is the minimum Manhattan distance from any cell on the path to any thief. Return the maximum safeness factor over all paths.

## Approach

Two phases.

### Phase 1 — distance to the nearest thief (multi-source BFS)

Compute `dist[r][c]` = Manhattan distance from each cell to the closest thief. Seed a BFS queue with **all** thief cells at distance 0 simultaneously, then expand outward. BFS visits cells in layers of increasing distance, so the first time a cell is reached, that layer is its distance to the *nearest* thief. On a 4-directional grid, BFS step count equals Manhattan distance. This fills the whole grid in **O(n²)** (one shared BFS — a separate BFS per thief would be O(n⁴)).

### Phase 2 — max-min path (Dijkstra with a max-heap)

The safeness of a path is the **minimum `dist`** over its cells; we want to **maximize** that minimum — a classic max-min / bottleneck path problem.

Run a Dijkstra variant where `best[r][c]` is the largest achievable path-minimum to reach `(r, c)`. Using a max-heap (Python's `heapq` is a min-heap, so push negated safeness), always expand the reachable cell with the highest safeness so far, carrying the running minimum:

```
cand = min(safe_so_far, dist[neighbor])
```

Relax a neighbor only when `cand` beats its current `best`. The first time the destination is popped, its running minimum is the answer.

## Complexity

- **Time:** O(n²) for the BFS + O(n² log n) for the heap-based search → **O(n² log n)**.
- **Space:** O(n²) for the `dist`, `best`, and heap structures.

## Notes

- The answer is capped by `dist[0][0]` and `dist[n-1][n-1]`, since every path includes the start and end cells; the running-minimum relaxation seeds `best[0][0] = dist[0][0]` to account for this.
- No thieves → every distance is effectively infinite; the BFS never seeds and this case should be handled per the problem's definition (LeetCode guarantees at least one thief).
- Alternative Phase-2 methods with the same complexity: **binary search on the answer** `k` (BFS over cells with `dist ≥ k`), or **Union-Find** adding cells in decreasing `dist` order until start and end connect.
