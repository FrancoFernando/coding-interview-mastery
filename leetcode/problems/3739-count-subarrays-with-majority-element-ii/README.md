# 3739. Count Subarrays With Majority Element II

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-ii/)

## Problem Description

Given an integer array `nums` and an integer `target`, return the number of subarrays in which `target` is the **majority element** — i.e. it appears **strictly more than half** the times in that subarray.

This is the same task as [3737](../3737-count-subarrays-with-majority-element-i), but with `n ≤ 10^5`, so an O(n²) pair count is too slow.

## Approach

The setup is identical to 3737:

1. **Transform** each element to `+1` if it equals `target`, else `-1`. A subarray has `target` as strict majority iff `(#target) - (#non-target) > 0`, i.e. its transformed sum is positive.
2. **Prefix sums** `prefix[0..n]` with `prefix[0] = 0`. The sum of `nums[i..j-1]` is `prefix[j] - prefix[i]`, so a subarray is valid iff `prefix[j] > prefix[i]` for `i < j`.
3. The answer is the number of index pairs `i < j` with `prefix[i] < prefix[j]`.

What changes is **only step 3's counting**. The brute O(n²) double loop becomes ~10¹⁰ operations at `n = 10^5`, so we count those pairs in **O(n log n)** with a Fenwick tree (Binary Indexed Tree).

| | 3737 (Medium) | 3739 (Hard) |
|---|---|---|
| `n` | ≤ 1000 | ≤ 10⁵ |
| Count pairs | nested loop, O(n²) | Fenwick sweep, O(n log n) |

### The pair count as a sweep

Restated, step 3 is the classic *"for each position, how many earlier values are strictly smaller?"* Sweep `prefix` left to right, keeping a frequency table of values seen so far. At each value `v`:

1. Query how many already-seen values are `< v` → add to the answer.
2. Insert `v`.

Querying *before* inserting is what enforces `i < j`. Starting the sweep on `prefix[0] = 0` is what lets subarrays beginning at index 0 be counted.

The frequency table needs two operations fast: "add 1 at value `v`" and "how many are `< v`" (a prefix sum over values). A plain array gives O(1) update but O(n) prefix query; a prefix-sum array gives O(1) query but O(n) update. A **Fenwick tree** does both in O(log n).

## Fenwick tree (Binary Indexed Tree)

A Fenwick tree is a 1-based array that supports, both in O(log n):

- `update(i, +1)` — add to position `i`
- `query(i)` — sum of positions `1..i`

### The trick: lowbit

Each index `i` is responsible for a range of length `i & (-i)` — its lowest set bit. (`-i` is two's complement: flip all bits and add 1, so `i & -i` isolates the lowest 1-bit.)

```
i = 6 = 110₂  → lowbit 2  → covers positions 5..6
i = 8 = 1000₂ → lowbit 8  → covers positions 1..8
i = 7 = 111₂  → lowbit 1  → covers position 7 only
```

- **query(i)** walks *down*: add `tree[i]`, then `i -= i & -i`, until `i == 0`.
- **update(i)** walks *up*: add to `tree[i]`, then `i += i & -i`, past the end.

Each walk visits ~log n nodes.

```python
class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)   # 1-based; index 0 unused

    def update(self, i, delta=1):
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & -i

    def query(self, i):             # sum of 1..i
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
```

Two non-negotiable rules:

- **1-based indexing.** Index 0 must stay unused: `i -= i & -i` from 0 never starts, and `i += i & -i` from 0 loops forever. Every value inserted must map to `≥ 1`.
- **Size** the tree to the largest index you will ever touch.

### Wiring it to this problem

Prefix values lie in `[-n, n]`, so offset them into `[1, 2n+1]`:

```python
offset = len(nums) + 1   # v = -n → 1, v = 0 → n+1, v = n → 2n+1
idx(v) = v + offset
```

Then querying **strictly less than** `v` is `query(idx(v) - 1)`. The smallest `v = -n` gives `query(0) = 0`, so there is no underflow.

## Complexity

- **Time:** O(n log n) — one Fenwick `query` + `update` per prefix value.
- **Space:** O(n) for the prefix array and the Fenwick tree.

## Notes

- Identical math to 3737 — only the pair-counting bookkeeping changes from a re-scan (O(n) per index) to a Fenwick lookup (O(log n) per index).
- Query is `idx(v) - 1` (strictly less than), **not** `idx(v)` — using `≤` would wrongly count equal prefixes, which correspond to zero-sum (tied) subarrays.
- An equivalent O(n log n) approach counts the pairs with a merge sort (inversion counting) over the prefix array.
