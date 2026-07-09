# 1288. Remove Covered Intervals

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/remove-covered-intervals/)

## Problem Description

Interval `[a, b)` is **covered** by `[c, d)` iff `c <= a` and `b <= d`. Remove every covered interval and return how many remain.

## Approach

Covering requires a coverer to **start at or before** and **end at or after**. So process intervals in an order where any potential coverer is seen first — that means **sort by start ascending**. After that, the `c <= a` half is handled by order (every earlier interval starts `<=` the current one), and coverage reduces to a single question: *has any earlier interval ended at or past the current end?* Track just the **maximum end seen so far**.

An interval survives iff it ends strictly farther right than everything before it:

```python
for start, end in sorted(intervals, key=lambda i: (i[0], -i[1])):
    if end > max_end:      # sticks out further right → not covered
        cnt += 1
        max_end = end
```

### The tie-break (the subtle part)

When two intervals share a start (e.g. `[1,4]` and `[1,6]`), the longer one covers the shorter. Sorting by start alone leaves their order arbitrary. Break ties by **end descending** (`key=(start, -end)`) so the longer interval is processed first, sets a high `max_end`, and the shorter same-start interval that follows is correctly detected as covered.

`end > max_end` (strict) with `<=` meaning "covered" is right: a later-starting interval that ends at the same `max_end` is genuinely covered, and equal-start-equal-end can't occur since intervals are unique.

## Complexity

- **Time:** O(n log n), dominated by the sort.
- **Space:** O(1) beyond the sort (or O(n) for the sorted copy).

## Notes

- General principle: pick the sort key by asking *"what order lets a simple running statistic answer the question?"* Here: coverers before coverees → start ascending; same-start ties resolved so the coverer leads → end descending; the statistic is `max_end`.
- Sorting end **ascending** instead would wrongly keep same-start covered intervals (e.g. `[[1,4],[1,6]]` → 2 instead of 1).
