# 3020. Find the Maximum Number of Elements in Subset

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/)

## Problem Description

Given an array of positive integers `nums`, select a subset that can be arranged as `[x, x², x⁴, …, xᵏ, …, x⁴, x², x]` (`k` a non-negative power of 2). Return the maximum size of such a subset.

## Approach

Stop thinking about arranging an array and think about **counting copies of powers**.

The pattern is a **palindrome ladder** built from a single base `x`, each level the previous one squared (`x → x² → x⁴ → …`):

- Every level **below the peak** appears **twice** (once climbing up, once coming down) → needs `count ≥ 2`.
- The **peak** appears **once** → needs `count ≥ 1`.

So only the multiset of values matters. Build a `Counter`, and for each base `x` greedily climb the chain:

```
val = x, length = 0
while count[val] >= 2:      # this level can be a paired rung
    length += 2
    val = val * val         # square to the next level
```

When the loop stops, `count[val] < 2`:

- `count[val] >= 1` → that value is the single **peak**: `length += 1`.
- `count[val] == 0` → can't cap here; drop back a rung, turning one paired element into the peak: `length -= 1` (only reachable after `length ≥ 2`, so the result stays odd and `≥ 1`).

The answer is the max `length` over all bases.

### The `x = 1` special case

`1² = 1`, so the chain never grows and the climb would loop forever — handle `1` separately and `continue` past it in the loop. A block of `c` ones must have **odd** length (peak + symmetric pairs), so it contributes `c` if `c` is odd, else `c − 1`.

## Complexity

- **Time:** O(U · log(max)) where `U` is the number of distinct values. Each climb squares `val`, so it reaches 10⁹ in ~30 steps.
- **Space:** O(U) for the counter.

## Notes

- Iterate over the **Counter's keys**, not `nums` — otherwise each base is restarted once per duplicate.
- `Counter[missing]` returns `0` without inserting the key, so reading `count[val]` inside `for base in count` is safe (no "dict changed size" error) and the missing-value lookup naturally terminates the climb.
- The longest chain is always discovered from its smallest base; larger bases only reproduce shorter sub-chains, so iterating all keys is correct (just mildly redundant).
- Overflow: in Python `val * val` is unbounded. In C++/Java bound the climb (e.g. stop once `val > 10⁹`) since `val²` overflows 64-bit fast.
