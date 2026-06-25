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

### The insight

The three rules together force the **sign of consecutive differences to alternate**: every valid array is a strict zigzag (`up, down, up, …` or `down, up, down, …`). Only the relative order of values matters, so shift the range to `1..m` where `m = r - l + 1`; the actual `l`/`r` don't matter beyond their count.

### Step 1 — What must we remember as we build left to right?

Build the array one element at a time. Sitting at position `i`, about to choose the next value, what's the minimum state that decides whether a choice is legal? The zigzag rule is **local**: legality of `a[i+1]` depends only on

1. the **last value** `v` (to compare against the next value), and
2. the **direction of the last step** (up or down — because the next step is forced to be the opposite).

The whole prefix before `a[i]` is irrelevant. That's why we need *two* tables, not one: `[2,5]` and `[8,5]` both end at `5`, but one arrived going up and the other going down, and they permit different continuations.

### Step 2 — Define the states

For a sequence of length `i` over values `1..m`:

- `up[i][v]` = zigzags ending at value `v` whose last step went **up** (`a[i-1] < v`).
- `down[i][v]` = zigzags ending at `v` whose last step went **down** (`a[i-1] > v`).

### Step 3 — Derive the transition by asking "where did I come from?"

To count `up[i][v]`, run the last step backward: chop off the final element `v`. What remains is a valid length-`(i-1)` zigzag ending at some `u`, and we appended `v` with `u < v` (that's what an up-step into `v` means). Because directions alternate, the step *before* the up-step must have been **down** — so the shorter sequence is counted by `down[i-1][u]`. Sum over every legal source `u < v`:

- `up[i][v] = Σ_{u < v} down[i-1][u]`
- `down[i][v] = Σ_{u > v} up[i-1][u]`   *(mirror argument)*

In words: *to end at `v` going up, I must have been at some smaller `u` having just gone down.* The alternation rule is the entire reason `up` reads from `down` and vice versa.

### Step 4 — Base case

Start at `i = 2`, since any length-2 array with two distinct values is already a valid zigzag:

- `up[2][v] = v - 1`  (number of smaller previous values)
- `down[2][v] = m - v`  (number of larger previous values)

### Step 5 — Answer

Every valid array ends *somewhere*, going *some* direction:

`answer = Σ_v (up[n][v] + down[n][v]) mod 1e9+7`.

### Step 6 — Why prefix sums

The naive transition sums over all `u` per `v` → `O(m²)` per row → `O(n·m²)` ≈ 16e9, too slow for `n, m ≤ 2000`. But as `v` grows by 1, `up[i][v]` just gains one term:

`up[i][v] = up[i][v-1] + down[i-1][v-1]`

So one left-to-right pass accumulating a running **prefix** sum yields every `up` entry in `O(m)`; `down` is the same with a right-to-left **suffix** sum. The `pre`/`suf` arrays in the code *are* those cumulative sums. Net: `O(n·m)`.

### Hand trace (`n = 3`, `m = 2`)

| length   | `up[1] up[2]` | `down[1] down[2]` |
|----------|---------------|-------------------|
| 2 (base) | `0  1`        | `1  0`            |
| 3        | `0  1`        | `1  0`            |

`up[3][2] = Σ_{u<2} down[2][u] = down[2][1] = 1`; `down[3][1] = Σ_{u>1} up[2][u] = up[2][2] = 1`. Total = `0+1+1+0 = 2` ✓ (matches Example 1).

## Complexity

- **Time:** O(n · m), where `m = r - l + 1`.
- **Space:** O(m) — two rolling rows.

## Notes

- Symmetry `up[i][v] = down[i][m+1-v]` could halve the work; kept both rows for clarity.
- The problem guarantees `n ≥ 3`. If generalizing, handle `n = 1` (→ `m`) and `n = 2` (→ `m·(m−1)`) separately, since the loop assumes the `i = 2` base.
- For astronomically large `n` with small `m`, the per-step linear map can be raised by matrix exponentiation in `O(m³ log n)`.
