# 1331. Rank Transform of an Array

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/rank-transform-of-an-array/)

## Problem Description

Replace each element with its **rank**: ranks start at 1, larger values get larger ranks, equal values share a rank, and ranks are as small as possible (no gaps).

## Approach

"As small as possible with equal values sharing a rank" means a value's rank is its **1-based position among the distinct sorted values**.

1. `sorted(set(arr))` — dedup (equal ⇒ same rank) and order in one step.
2. Build a `value → rank` map: `{val: idx + 1 for idx, val in enumerate(unique_sorted)}`.
3. Map every original element through it, preserving input order.

```python
unique_sorted = sorted(set(arr))
num_to_rank = {val: idx + 1 for idx, val in enumerate(unique_sorted)}
return [num_to_rank[n] for n in arr]
```

## Complexity

- **Time:** O(n log n) — the sort dominates; lookups are O(n) total.
- **Space:** O(n) for the set and the rank map.

## Notes

- **Empty array** falls out naturally: `sorted(set([]))` is `[]`, so the comprehension returns `[]` with no special case.
- Deduping is what enforces both "equal ⇒ same rank" and "no gaps" — without `set`, duplicates would consume rank numbers and leave gaps.
