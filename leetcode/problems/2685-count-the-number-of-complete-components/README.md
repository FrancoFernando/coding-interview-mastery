# 2685. Count the Number of Complete Components

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/count-the-number-of-complete-components/)

## Problem Description

Given an undirected graph on `n` vertices, return the number of **complete** connected components — components in which every pair of vertices is joined by an edge.

## Approach

A connected component of `k` vertices is complete iff there is an edge between every pair. Two equivalent tests:

- It has exactly `k·(k-1)/2` edges, or
- **every vertex has degree `k-1`** (joined to all others).

The degree form is used here since the adjacency list gives each vertex's degree directly (no double-count halving needed).

Steps:

1. Build an adjacency list.
2. For each unvisited vertex, BFS to collect its whole component (a helper returns the node list and marks them visited).
3. Let `k` be the component size; it's complete iff `all(len(graph[v]) == k - 1 for v in nodes)`.

The BFS is extracted into a `collect_component` closure, which names the intent and removes the need for any component-id bookkeeping — the helper hands back the node list directly.

## Complexity

- **Time:** O(n + E) — each vertex and edge visited once.
- **Space:** O(n + E) for the adjacency list, queue, and visited array.

## Notes

- **Isolated vertices are complete** (`k = 1` needs 0 edges, degree `0 == 0`); the degree test handles them with no special case.
- A component shares no edges with the outside, so every edge incident to its vertices is internal — that's why the per-vertex degree equals its within-component degree.
- Union-Find is an equally valid alternative: track size and internal edge count per root, then test `edges == size·(size-1)/2`.
