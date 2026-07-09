# 2492. Minimum Score of a Path Between Two Cities

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/)

## Problem Description

Cities `1..n` connected by bidirectional weighted roads (graph not necessarily connected). The **score** of a path is the minimum road distance on it. Return the minimum possible score of a path between city `1` and city `n`.

## Approach

The rules that a path may **reuse roads** and **revisit cities** collapse the problem entirely:

- Any edge in city `1`'s connected component can be woven onto a `1 → n` path (go to that edge, traverse it, continue to `n`).
- `n` is guaranteed to be in that same component (a path exists).
- The score is the **minimum** edge on the path, and we want to **minimize** it, so we can always drag in the single cheapest edge of the component.

So the answer is just the **minimum edge weight in the connected component containing city 1** — no routing or shortest-path needed.

Traverse that component (BFS or DFS) and track the smallest edge weight seen:

```python
visited = {1}
q = deque([1])
min_score = inf
while q:
    node = q.popleft()
    for adj, dist in graph[node]:
        min_score = min(min_score, dist)   # every incident edge
        if adj not in visited:
            visited.add(adj)
            q.append(adj)
```

## Complexity

- **Time:** O(V + E) — one traversal of the component.
- **Space:** O(V + E) for the adjacency list, queue, and visited set.

## Notes

- **Update `min_score` on every incident edge**, not only edges to unvisited nodes — the cheapest edge may connect two already-visited nodes. Skip only the *enqueue* for visited nodes. This is the easy-to-miss bug.
- No need to detect reaching `n` or stop early; the min edge may hang off any node, so sweep the whole component.
- Cities are 1-indexed, so size the adjacency list `n + 1`.
- **Union-Find** is an equally valid alternative: union all roads, then take `min(d for a, b, d in roads if find(a) == find(1))`.
