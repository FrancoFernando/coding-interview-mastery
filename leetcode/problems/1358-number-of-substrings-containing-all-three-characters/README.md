# 1358. Number of Substrings Containing All Three Characters

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

## Problem Description

Given a string `s` of only `a`, `b`, `c`, return the number of substrings containing at least one occurrence of all three characters.

## Approach

Count valid substrings by their **right endpoint** `r`, in a single pass.

Track the **last index where each character appeared** (`last_seen[a/b/c]`). A substring ending at `r` contains all three characters iff its left start is `≤` the last-seen index of *every* character — i.e. `start ≤ min(last_seen)`. So the number of valid starts for this `r` is:

```python
min(last_seen.values()) + 1     # when all three have appeared
```

While any character is still unseen, its last-seen value is `-1`, so `min == -1` and the contribution is skipped. Summing over all `r` gives the answer.

```python
last_seen = {'a': -1, 'b': -1, 'c': -1}
result = 0
for r in range(len(s)):
    last_seen[s[r]] = r
    earliest = min(last_seen.values())
    if earliest != -1:
        result += 1 + earliest
return result
```

### Why this works

For a fixed left start `i`, once a window `s[i..j]` contains all three, every longer window `s[i..k]` (`k ≥ j`) is also valid — adding characters never removes one. This problem buckets that same counting by right endpoint instead of left: `min(last_seen)` is the furthest-left a valid substring ending at `r` can start.

## Complexity

- **Time:** O(n) — one pass; `min` is over a fixed 3-element dict, so O(1) per step.
- **Space:** O(1) — three counters.

## Notes

- Computing `earliest = min(...)` once and reusing it avoids scanning the values twice (once to check "all seen", once for the contribution). `earliest != -1` is exactly the "all three seen" test.
- Equivalent O(n) framings: a sliding window that, for each left `i`, finds the smallest valid right `j` and adds `n - j` (the right pointer is monotonic non-decreasing).
