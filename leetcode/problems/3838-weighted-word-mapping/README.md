# 3838. Weighted Word Mapping

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/weighted-word-mapping/)

## Problem Description

You are given a list of `words` (lowercase letters only) and a list `weights` of length 26, where `weights[i]` is the weight assigned to the letter at alphabet position `i` (so `weights[0]` is the weight of `'a'`, `weights[25]` is the weight of `'z'`).

For each word, compute the sum of the weights of its characters. Map that sum to a single output letter via:

```text
out_char = chr(ord('z') - (sum % 26))
```

Return the concatenation of the mapped letters, one per input word.

## Approach

For each word, sum `weights[ord(c) - ord('a')]` over its characters, take the result mod 26, and subtract from `ord('z')` to produce the output letter. The whole thing collapses into a single generator passed to `''.join`, with `ord('a')` and `ord('z')` hoisted out of the inner loop so they are computed once instead of once per character.

## Complexity

- **Time Complexity:** O(total characters across all words). Each character is touched exactly once.
- **Space Complexity:** O(W) for the output string, where W is the number of words. The generator avoids building any intermediate list.

## Notes

- `str.join` consumes a generator directly — no need for an intermediate `result = []; result.append(...)` loop.
- The mod-26 step means `sum == 26` and `sum == 0` both map to `'z'`; `sum == 1` maps to `'y'`; `sum == 25` maps to `'a'`.
- For larger alphabets or repeated calls, you could precompute a `dict` mapping `char -> weight` once, but for 26 fixed letters `ord(c) - a` is already O(1) and faster than a dict lookup.
