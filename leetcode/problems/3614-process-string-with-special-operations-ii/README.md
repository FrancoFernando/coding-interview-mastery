# 3614. Process String with Special Operations II

**Difficulty:** Hard  
**Link:** [LeetCode](https://leetcode.com/problems/process-string-with-special-operations-ii/)

## Problem Description

You are given a string `s` of lowercase English letters plus the special characters `'*'`, `'#'`, and `'%'`, and an integer `k`.

Build `result` by processing `s` left to right:

- a lowercase letter is appended to `result`
- `'*'` removes the last character of `result`, if it exists
- `'#'` duplicates `result` and appends it to itself
- `'%'` reverses `result`

Return the `k`th character of the final `result`, or `'.'` if `k` is out of bounds.

Constraints: `1 <= s.length <= 10^5`, `0 <= k <= 10^15`, and the final length of `result` does not exceed `10^15`.

## What changed from Part I

The operations are identical. Only the **constraints** changed:

| | Part I | Part II |
|---|---|---|
| `result` length | small (fits in memory) | up to **10^15** |
| `k` | small | up to **10^15** |

In Part I you simply **simulate**: build the string with a list, apply each op, return `result[k]`.

In Part II that's impossible. `'#'` *doubles* the length, so with up to 10^5 ops the string would reach 2^(10^5) characters — you can never materialize it (time and memory both die). The hard version forces you to answer "what character sits at index `k`?" **without ever building the string**.

## Approach

Two passes, both O(n).

**Step 1 — Forward pass: track only the length.**

Walk `s` once and record `lengths[i]` = the length of `result` *after* applying op `i`:

- letter → `length + 1`
- `'*'` → `max(length - 1, 0)`
- `'#'` → `length * 2` (capped, so the integer never explodes)
- `'%'` → unchanged

If `k >= final length`, return `'.'`.

**Step 2 — Backward pass: trace index `k` to its origin.**

Walk the ops in reverse. At each op, `k` is an index into the string *after* that op; translate it to the index *before*:

- **letter `c`** (length grew by 1): if `k` is the last index (`length - 1`), the answer is `c`; otherwise `k` is unchanged.
- **`'%'` (reverse)**: the char at `k` came from `length - 1 - k` before reversing → `k = length - 1 - k`.
- **`'#'` (duplicate)**: let `half = length // 2`. If `k >= half`, it lives in the copied half → `k -= half`. The character is identical either way.
- **`'*'` (remove)**: only the last char was dropped; every index below it is untouched → `k` unchanged.

Stop the moment a letter op claims index `k`. No string is ever built.

### Why the cap is safe

We cap lengths at a value above `10^15` so a long run of `'#'` can't create a giant Python integer. Capping only ever happens for lengths far beyond `10^15`, and since `k < 10^15`, `k` is always below the capped `half` — so it is correctly treated as living in the first half, exactly as it would be at the true length.

## Complexity

- **Time Complexity:** O(N) — one forward pass and one backward pass over `s`
- **Space Complexity:** O(N) — the per-step lengths array

## Notes

The medium→hard jump here is a classic pattern: the task shifts from "produce the whole structure" to "trace one element's provenance through transformations you can't afford to perform."
