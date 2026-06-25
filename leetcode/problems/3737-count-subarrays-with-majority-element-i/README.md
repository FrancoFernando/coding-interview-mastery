# 3737. Count Subarrays With Majority Element I

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/count-subarrays-with-majority-element-i/)

## Problem Description

Given an integer array `nums` and an integer `target`, return the number of subarrays in which `target` is the **majority element** — i.e. it appears **strictly more than half** the times in that subarray.

## Approach

The "strict majority" condition can be rewritten cleanly. If a subarray has length `L` and contains `k` copies of `target`:

```
k > L / 2  ⟺  k > (L - k)  ⟺  k - (L - k) > 0
```

The quantity `k - (L - k)` is `(#target) - (#non-target)`. So map each element to:

- `+1` if it equals `target`
- `-1` otherwise

Now a subarray is valid **iff its transformed sum is positive**.

Build a prefix-sum array `prefix` of length `n + 1` with `prefix[0] = 0`. The sum of `nums[i..j-1]` is `prefix[j] - prefix[i]`, so a subarray is valid iff `prefix[j] > prefix[i]` for `i < j`. The answer is the number of index pairs `i < j` with `prefix[i] < prefix[j]`.

With `n ≤ 1000`, an O(n²) double loop over prefix pairs is comfortable.

## Complexity

- **Time:** O(n²) — count all pairs of prefix indices.
- **Space:** O(n) for the transformed and prefix arrays.

## Notes

- Including `prefix[0] = 0` is what lets subarrays starting at index 0 be counted; `j` must range up to `n` so subarrays ending at the last element are included.
- The pair-counting step is the classic "count earlier elements smaller than the current one." For the harder follow-up (large `n`), replace the O(n²) loop with a Binary Indexed Tree / merge sort over coordinate-compressed prefix values for O(n log n).
- `itertools.accumulate(transformed, initial=0)` produces the `n + 1`-length prefix array directly.
