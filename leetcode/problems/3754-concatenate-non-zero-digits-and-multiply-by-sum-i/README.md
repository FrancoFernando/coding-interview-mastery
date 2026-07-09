# 3754. Concatenate Non-Zero Digits and Multiply by Sum I

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/)

## Problem Description

Form `x` by concatenating all **non-zero** digits of `n` in their original order (`x = 0` if there are none). Let `sum` be the sum of `x`'s digits. Return `x * sum`.

## Approach

Direct simulation with pure arithmetic — no string allocation.

Peel digits right-to-left with `divmod(n, 10)`:

- `digit_sum` accumulates **every** digit (zeros add `0`, so no guard needed).
- `new_x` rebuilds the number from **only non-zero** digits, placing each at the next power of ten via `mult`. Because `mult` advances only when a non-zero digit is placed, the zeros drop out with no gaps.

```python
while n > 0:
    n, d = divmod(n, 10)
    digit_sum += d
    if d:
        new_x += d * mult
        mult *= 10
return new_x * digit_sum
```

Building right-to-left is why `mult` (rather than `new_x = new_x*10 + d`) is used: the least-significant kept digit must land at `mult = 1`.

## Complexity

- **Time:** O(#digits of n).
- **Space:** O(1) — no string conversion.

## Notes

- `n = 0` (or any all-zero case): loop skips, returns `0 * 0 = 0`.
- A string variant is more declarative but allocates:
  `digits = [int(d) for d in str(n) if d != '0']; return (int(''.join(map(str, digits))) if digits else 0) * sum(digits)`.
  The arithmetic version wins on efficiency; the string version on readability.
