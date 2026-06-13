# 3691. Maximum Total Subarray Value II

**Difficulty:** Hard  
**Link:** [LeetCode](https://leetcode.com/problems/maximum-total-subarray-value-ii/)

## Problem Description

You are given an integer array `nums` of length `n` and an integer `k`.

You must select exactly `k` **distinct** subarrays `nums[l..r]`. Subarrays may
overlap, but the same `(l, r)` cannot be chosen twice.

The value of a subarray is `max(nums[l..r]) - min(nums[l..r])`. The total value
is the sum of the values of the chosen subarrays. Return the maximum possible
total value.

**Example 1:** `nums = [1,3,2], k = 2` -> `4`
**Example 2:** `nums = [4,2,5,1], k = 3` -> `12`

Constraints: `1 <= n <= 5*10^4`, `0 <= nums[i] <= 10^9`,
`1 <= k <= min(10^5, n*(n+1)/2)`.

## Approach

### 1. Reframe the selection

The chosen subarrays are independent and every value is `>= 0`, so maximizing
the sum just means **picking the `k` subarrays with the largest value**. The
problem becomes: sum of the top-`k` values of `max - min` over all subarrays.
There are `O(n^2)` subarrays (~2.5e9), so we can't list them all — we need to
pull out the top-`k` lazily.

### 2. The monotonicity that makes a heap work

If window B contains window A, then `value(B) >= value(A)` — a bigger window can
only push `max` up and `min` down. Two consequences:

- The **whole array `[0, n-1]` has the global maximum value** (our starting point).
- **Shrinking** a window (dropping one end) can only keep the value equal or smaller.

So values decrease as we move to sub-windows. That's exactly the setup for a
**best-first search with a max-heap**: start at the known maximum and expand the
current best into slightly smaller windows.

### 3. Generate children without duplicates

From `[l, r]` the two shrink moves are `[l+1, r]` and `[l, r-1]`. Pushing both
freely revisits the same window from two directions (you can reach `[1,2]` via
left-then-right or right-then-left). Fix it by forcing one canonical order:

- always push `[l+1, r]` (shrink left), and
- push `[l, r-1]` (shrink right) **only when `l == 0`**.

Meaning: shrink the right end only while the left is still untouched; once you've
shrunk the left even once, the right end is frozen. This makes every subarray
reachable by exactly one path, turning the lattice into a **tree** — so no
duplicates and no `visited` set. Since each parent strictly contains its child,
the heap pops values in non-increasing order, which is the top-`k` guarantee.

### 4. Price any window in O(1) with a sparse table

The heap needs `max - min` for arbitrary `[l, r]` jumping around, so an
incremental "update from the parent" trick fails (when the element you drop *is*
the current max/min, you'd have to rescan). A **sparse table** precomputes
range-max/range-min for every power-of-two block (`O(n log n)` build) and answers
any range in `O(1)` by overlapping two blocks — overlap is fine because
`max(a, a) = a`. Build one table for max and one for min.

### Putting it together

Seed the heap with `[0, n-1]`, pop `k` times summing the values, and expand each
popped window with the dedup rule above. See `solution.py`.

> Tip: the logic is correct even with a slow `max(nums[l:r+1])` pricing — that
> version gives the right answer but TLEs at `O(k*n)`. The sparse table only
> swaps the per-window lookup from `O(n)` to `O(1)`; the heap loop is identical.

## Complexity

- **Time Complexity:** `O(n log n)` to build the sparse tables + `O(k log k)` for the heap.
- **Space Complexity:** `O(n log n)` for the two sparse tables.

## Notes

- This is the same heap + dedup pattern as enumerating the k largest/smallest
  "expandable" things (cf. k-th smallest in a sorted matrix) — a tree of states
  where each edge only decreases the key.
- Python `heapq` is a min-heap, so we store `-value` to simulate a max-heap.
- `k <= n*(n+1)/2` is guaranteed, so the heap never empties before `k` pops.
