# 3700. Number of ZigZag Arrays II

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/number-of-zigzag-arrays-ii/)

## Problem Description

Given three integers `n`, `l`, and `r`, count the ZigZag arrays of length `n` where:

- Each element lies in `[l, r]`.
- No two adjacent elements are equal.
- No three consecutive elements form a strictly increasing or strictly decreasing run.

Return the count modulo `10^9 + 7`.

**This is the same problem as [3699. Number of ZigZag Arrays I](../3699-number-of-zigzag-arrays-i), but the limits flip:** here `3 <= n <= 1e9` while `1 <= l < r <= 75`. So `m = r - l + 1 <= 75` is tiny, but `n` is enormous.

## Approach

### Why Part I's DP no longer works

The combinatorial core is identical to Part I: every valid array is a strict **zigzag** (the difference signs alternate), and only the count of values `m = r - l + 1` matters, not `l`/`r` themselves. Part I solves it with an `O(n·m)` row-by-row DP.

Here `n` can be `1e9`, so `O(n·m)` is up to `~7.5e10` operations — far too slow. But `m <= 75` is small. That combination (huge step count, small state) is the textbook signal for **matrix exponentiation**: if each DP step is the *same* linear map `A`, then advancing `k` steps is `A^k`, computable in `O(log k)` matrix multiplies.

### Step 1 — Collapse the state with symmetry

Part I tracks two length-`m` rows, `up[v]` and `down[v]` (zigzags ending at `v` with the last step going up / down). Reversing every value (`v → m+1-v`) is a bijection on zigzag arrays that swaps the last step's direction, so

```
down[v] = up[m + 1 - v]
```

at every length. The `up` vector alone is therefore complete state — halving the dimension from `2m` to `m` (a 4× speedup, since cost is cubic).

### Step 2 — Write one step as a matrix

The Part I transition was `up'[v] = Σ_{u<v} down[u]`. Substitute the symmetry and reindex with `j = m+1-u`:

```
up'[v] = Σ_{u<v} up[m+1-u] = Σ_{j >= m+2-v} up[j]
```

That is a linear map `up' = A · up` with a clean 0/1 **anti-triangular** matrix (1-indexed):

```
A[v][j] = 1   iff   v + j >= m + 2
```

Each `up'[v]` is just a suffix sum of `up` — the matrix form simply makes that map explicit so we can exponentiate it. (0-indexed in code: `A[i][k] = 1` iff `i + k >= m`.)

### Step 3 — Jump n steps at once

`A` is identical at every step, so going from the length-2 state to length `n` is `A^(n-2)`. Compute it by binary exponentiation (square-and-multiply): `O(log n)` multiplies of `m × m` matrices.

### Step 4 — Base case and answer

The length-2 vector is `up[v] = v - 1` (Part I's base). Apply the power, then use symmetry once more to fold `down` back in:

```
answer = Σ_v (up[n][v] + down[n][v]) = 2 · Σ_v up[n][v]   (mod 1e9+7)
```

because `Σ_v down[n][v] = Σ_v up[n][m+1-v] = Σ_v up[n][v]`.

### Sanity checks

- `m = 2`, `A` is 1 only at `[2][2]`; the up-vector stays `[0, 1]` forever, so the answer is `2` for any `n` (the two arrays `4,5,4,…` and `5,4,5,…`). ✓
- `n = 3, m = 3`: `A^1 · [0,1,2] = [0,2,3]`, sum `5`, answer `10`. ✓ (Example 2)

## Complexity

- **Time:** O(m³ · log n) — `log n` matrix multiplies, each `O(m³)`. With `m ≤ 75`, trivially fast.
- **Space:** O(m²) for the matrices.

## Notes

- **Same recurrence, two scaling regimes.** Part I (`n, m ≤ 2000`) wants the `O(n·m)` prefix-sum DP; Part II (`n ≤ 1e9`, `m ≤ 75`) wants `O(m³ log n)` matrix power. Recognizing that a per-step DP transition is a *fixed linear map* is the reusable trick.
- The symmetry reduction is an optimization, not a necessity — you can exponentiate the full `2m × 2m` transition matrix instead; it's `8×` slower but needs no reversal argument.
- In Python, reduce mod `1e9+7` inside the dot-product accumulation. A naive `numpy` `int64` matmul overflows: up to `m` products of `~1e9 · 1e9` sum past `int64`'s `~9.2e18` range.
- The matrix `A[i][k] = [i + k >= m]` is anti-triangular; structure-aware multiplication could shave the constant factor, but it's unnecessary at `m ≤ 75`.
