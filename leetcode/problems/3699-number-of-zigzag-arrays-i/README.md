# 3699. Number of ZigZag Arrays I

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-i/)

## Problem Description

Given three integers `n`, `l`, and `r`, count the ZigZag arrays of length `n` where:

- Each element lies in `[l, r]`.
- No two adjacent elements are equal.
- No three consecutive elements form a strictly increasing or strictly decreasing run.

Return the count modulo `10^9 + 7`.

## Approach

The three rules together force the **sign of consecutive differences to alternate**: every valid array is a strict zigzag (`up, down, up, …` or `down, up, down, …`). Only the relative order of values matters, so shift the range to `1..m` where `m = r - l + 1`; the actual `l`/`r` don't matter beyond their count.

DP on the direction of the last step. For a sequence of length `i`:

- `up[i][v]` = zigzags ending at value `v` whose last step went **up** (`a[i-1] < v`).
- `down[i][v]` = zigzags ending at `v` whose last step went **down**.

Transitions flip the direction each step:

- `up[i][v] = Σ_{u < v} down[i-1][u]`
- `down[i][v] = Σ_{u > v} up[i-1][u]`

Base case at `i = 2` (any length-2 array is a valid zigzag):

- `up[2][v] = v - 1` (smaller previous values)
- `down[2][v] = m - v` (larger previous values)

Answer = `Σ_v (up[n][v] + down[n][v]) mod 1e9+7`.

The naive transition sums over all `u` per `v` → `O(n·m²)`, too slow for `n, m ≤ 2000`. But each transition is a **prefix sum** (`up`) or **suffix sum** (`down`) of the previous row, computed once per row, making each entry `O(1)`.

## Complexity

- **Time:** O(n · m), where `m = r - l + 1`.
- **Space:** O(m) — two rolling rows.

## Notes

- Symmetry `up[i][v] = down[i][m+1-v]` could halve the work; kept both rows for clarity.
- The problem guarantees `n ≥ 3`. If generalizing, handle `n = 1` (→ `m`) and `n = 2` (→ `m·(m−1)`) separately, since the loop assumes the `i = 2` base.
- For astronomically large `n` with small `m`, the per-step linear map can be raised by matrix exponentiation in `O(m³ log n)`.
