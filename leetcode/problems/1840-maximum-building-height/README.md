# 1840. Maximum Building Height

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/maximum-building-height/)

## Problem Description

You want to build `n` buildings labeled `1..n` in a line. Heights are non-negative integers, building 1 has height 0, and adjacent heights differ by at most 1. A list `restrictions[i] = [id_i, maxHeight_i]` caps the height of specific buildings. Return the maximum possible height of the tallest building.

Constraints: `2 ≤ n ≤ 10^9`, `restrictions.length ≤ 10^5`. So the algorithm must run in terms of `len(restrictions)`, not `n`.

## Approach

### Key generalization

The adjacency rule `|h[k+1] − h[k]| ≤ 1` chains across multiple steps: for any positions `a < b`,
```
h[b] ≤ h[a] + (b − a)
h[a] ≤ h[b] + (b − a)
```
A restriction at one position therefore constrains heights on *both* sides of it.

### Two-pass tightening

Add `(1, 0)` as an implicit restriction (building 1 is anchored at height 0) and sort by id.

- **Left → right sweep:** `h[i] ≤ h[i−1] + (id[i] − id[i−1])`. Each restriction inherits the cap implied by its left neighbor.
- **Right → left sweep:** `h[i] ≤ h[i+1] + (id[i+1] − id[i])`. Mirror image.

Both passes are needed because a single sweep only propagates tightness in one direction, but each restriction limits both sides.

### Right boundary

After the sweeps, if the last restriction sits at position `p < n`, buildings `p+1..n` can rise unimpeded. Append a synthetic entry `(n, h[p] + (n − p))` so the final peak loop handles it uniformly.

### Peak per segment

Between two adjacent restrictions `(l, hl)` and `(r, hr)` with `d = r − l`, the achievable height at any position `x ∈ [l, r]` is bounded from both sides:
```
h(x) ≤ hl + (x − l)
h(x) ≤ hr + (r − x)
```
The maximum is the "tent" peak where the two lines meet:
```
peak = (hl + hr + d) // 2
```

The answer is the maximum peak across all adjacent pairs in the tightened list.

## Complexity

- **Time:** O(m log m) where `m = len(restrictions)`. Sorting dominates; the two sweeps and the peak scan are linear.
- **Space:** O(m). `n` never appears in the runtime — confirms the algorithm is restriction-bound, not building-bound.

## Notes

- **Mutation gotcha:** `(li, lh), (ri, rh) = l, r` is fine for reading, but writing to `lh` or `rh` does *not* update the underlying list because Python ints are immutable. The sweep must mutate through `l[1]` / `r[1]` directly.
- The peak formula floors because heights must be integers — if `hl + hr + d` is odd, the geometric crossing falls between two grid positions and only the floor is achievable.
- Don't append the right-boundary entry before sorting: you'd be guessing the height and relying on the sweeps to fix it. Appending after, using the tightened last height, is cleaner.
