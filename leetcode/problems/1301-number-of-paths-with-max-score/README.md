# 1301. Number of Paths with Max Score

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/number-of-paths-with-max-score/)

## Problem Description

On a square board, move from `S` (bottom-right) to `E` (top-left) going up, left, or up-left, avoiding `X` obstacles, collecting the digits `1..9`. Return `[max sum, number of paths achieving it mod 1e9+7]`, or `[0, 0]` if `E` is unreachable.

## Approach

A **two-value DP**: track both the best score and how many paths achieve it, in lockstep.

- `score[i][j]` = maximum digit sum on a path from `S` to `(i, j)` (`-inf` = unreachable).
- `ways[i][j]` = number of paths achieving that maximum, mod `1e9+7`.

Moves are up / left / up-left, so a path arrives at `(i, j)` **from** the cells below / right / below-right: `(i+1, j)`, `(i, j+1)`, `(i+1, j+1)`. Iterating from bottom-right to top-left guarantees those predecessors are already computed.

### Transition (the crux is the counting)

Among the reachable predecessors, take the highest `score`. Then:

- A predecessor with a **strictly greater** score **replaces** the best and its count.
- A predecessor **tied** with the best **adds** its count.

```python
if score[pi][pj] > best:
    best, cnt = score[pi][pj], ways[pi][pj]   # replace
elif score[pi][pj] == best:
    cnt = (cnt + ways[pi][pj]) % MOD          # tie -> accumulate
```

Then `score[i][j] = best + value(i,j)` and `ways[i][j] = cnt`, where `S` and `E` contribute value 0 and digits contribute themselves.

### Base case & reachability

- `S`: `score = 0`, `ways = 1`.
- A cell whose predecessors are all unreachable stays `-inf` — never becoming a bogus 0. This is what makes a wall of `X` (Example 3) correctly yield `[0, 0]`: `E` stays unreachable.

## Complexity

- **Time:** O(n²) — constant work per cell.
- **Space:** O(n²) for the two tables.

## Notes

- **Never add a digit for `S` or `E`** — only `1..9` cells contribute.
- **Ties add, strict-greater replaces** — getting this exactly is what makes the second number correct.
- Keep `-inf` as an internal sentinel only; convert to `[0, 0]` at return (an infinite/float value can't be serialized as the required `int`).
- Bottom-up is natural here (uniform dependency order); a top-down memoized version is equally valid and makes "unreachable = a sentinel return" fall out for free.
