# 3756. Concatenate Non-Zero Digits and Multiply by Sum II

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/)

## Problem Description

Given a digit string `s` and queries `[l, r]`, for each substring `s[l..r]` form `x` by concatenating its non-zero digits (`x = 0` if none), let `sum` be the sum of `x`'s digits, and return `x * sum` mod `1e9+7`.

## Approach

This is the range-query version of [3754](../3754-concatenate-non-zero-digits-and-multiply-by-sum-i). Two things change: many substrings must be answered, and `x` can have thousands of digits, so it must be built **mod p** from the start. A segment tree works (store `(value mod p, non-zero count)` and merge), but for a **static** string a prefix identity gives O(1) per query with no tree and no modular inverse.

Build three prefix arrays over `s[0..i-1]`:

- `P[i]` = its non-zero digits concatenated, mod p
- `C[i]` = count of non-zero digits
- `D[i]` = sum of all digits (zeros add 0, so this equals the non-zero sum)

```
P[i+1] = (P[i]*10 + d) % p, C[i+1] = C[i]+1   if d != 0
P[i+1] = P[i],             C[i+1] = C[i]       if d == 0
```

### The identity

For a range `[l, r]`, the non-zero digits of `s[0..r]` split into the prefix block `P[l]` (digits before `l`) followed by the range block `X`:

```
P[r+1] = P[l] * 10^k + X,   k = C[r+1] - C[l]   (non-zero digits in range)
=>  X = (P[r+1] - P[l] * 10^k) mod p
```

It's a **subtraction**, so no modular inverse is needed. Then:

```
sum    = D[r+1] - D[l]
answer = X * sum  mod p
```

## Complexity

- **Time:** O(m) precompute (`P`, `C`, `D`, `pow10`) + O(1) per query.
- **Space:** O(m).

## Notes

- Python's `%` returns a non-negative result, so `X = (P[r+1] - P[l]*pow10[k]) % p` is already normalized. In C++/Java add `p` and re-mod to avoid a negative.
- Why not a plain prefix product? The left-shift amount `k` depends on the non-zero count *inside* the range — but `P[l]` is exactly the prefix block being shifted, so the general associative merge (what a segment tree does) collapses to this one subtraction for a static string.
- The `sum` half is trivial in both I and II — only `x` needed the mod-p machinery.
