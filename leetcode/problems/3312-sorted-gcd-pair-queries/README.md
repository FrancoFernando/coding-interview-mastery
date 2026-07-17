# 3312. Sorted GCD Pair Queries

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/sorted-gcd-pair-queries/)

## Problem Description

`gcdPairs` = sorted list of `gcd(nums[i], nums[j])` over all `i < j`. For each query `q`, return `gcdPairs[q]`.

## Approach

There are up to ~`n²/2` pairs (n up to 1e5 → billions), so `gcdPairs` cannot be built directly. But values are small (≤ ~5·10⁴), so **count how many pairs have each gcd value** with divisor inclusion–exclusion.

1. `freq[v]` = how many nums equal `v`.
2. For each `g` from high to low: let `d` = count of nums divisible by `g`. Pairs whose gcd is a **multiple of `g`** = `C(d, 2) = d(d-1)/2`. Subtract the exact counts of `2g, 3g, …` (already computed, since we go top-down) to get `exact[g]` = pairs with gcd **exactly** `g`.
   ```
   exact[g] = C(#divisible-by-g, 2) - Σ_{m = 2g, 3g, …} exact[m]
   ```
3. Prefix-sum `exact` → `prefix[g]` = number of pairs with gcd `≤ g`. This is the sorted `gcdPairs`, run-length encoded (non-decreasing, `prefix[0] = 0`).
4. Each query `q` → smallest `g` with `prefix[g] > q` = `bisect_right(prefix, q)`.

## Complexity

- **Time:** O(maxv log maxv) for the divisor sieve (`Σ maxv/g`), plus O(q log maxv) for the queries.
- **Space:** O(maxv) for `freq`, `exact`, `prefix`.

## Notes

- The nested `range(g, maxv+1, g)` loops are a harmonic sum → `O(maxv log maxv)` total, not `O(maxv²)`.
- Top-down order (`g` from `maxv` to `1`) is essential: `exact[m]` for multiples `m > g` must be finalized before computing `exact[g]`.
- `bisect_right(prefix, q)` returns the first index whose cumulative count exceeds `q` — exactly the value at sorted position `q` (0-indexed).
