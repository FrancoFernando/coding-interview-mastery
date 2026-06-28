# 1846. Maximum Element After Decreasing and Rearranging

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/)

## Problem Description

Given positive integers `arr`, you may **decrease** any element to a smaller positive integer and **rearrange** the elements freely. Make the array satisfy: `arr[0] == 1`, and `abs(arr[i] - arr[i-1]) <= 1` for all `i`. Return the maximum possible value of any element afterward.

## Approach

To maximize the final value you want the steepest legal staircase, which climbs by at most 1 per step. The question becomes: *given this multiset, what's the highest staircase I can build?*

**Sort ascending**, then walk through the values keeping a running height `prev`:

```python
prev = 0
for num in sorted(arr):
    prev = min(prev + 1, num)
return prev
```

The `min` enforces both operations at once:

- `prev + 1` — the adjacency rule: each element may exceed its predecessor by at most 1.
- `num` — the decrease-only rule: a value can be lowered but never raised, so it can't exceed what you actually hold.

So each step climbs by one when the value allows it, otherwise takes the (smaller) value as-is. Starting `prev = 0` forces the first element to `min(1, num) = 1`, satisfying `arr[0] == 1` with no special case.

The sequence is non-decreasing, so `prev` after the final step is the maximum — no separate max tracking needed.

**Why sorting is optimal:** smaller values only help when the staircase is low, so spend them early and save larger values for later. There is never a reason to place a larger available value before a smaller one.

## Complexity

- **Time:** O(n log n), dominated by the sort.
- **Space:** O(1) extra (a single running variable beyond the sort).

## Notes

- After sorting, the invariant `prev <= num` always holds (`prev` is a `min` that includes `num`, and the next `num` is never smaller), so `num < prev` is impossible. The `min` therefore matters only for the duplicate case `num == prev`; otherwise `num >= prev + 1` and the staircase climbs (capping down to `prev + 1` when `num > prev + 1`).
- No need to mutate the array; one `prev` variable suffices.
