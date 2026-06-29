# 1967. Number of Strings That Appear as Substrings in Word

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)

## Problem Description

Given an array of strings `patterns` and a string `word`, return how many strings in `patterns` appear as a substring of `word`.

## Approach

Python's `in` operator already performs a substring test, so the whole problem is a one-line count:

```python
return sum(1 for pattern in patterns if pattern in word)
```

For each `pattern`, `pattern in word` is `True` when it occurs contiguously in `word`; summing the truthy hits gives the answer.

## Complexity

- **Time:** O(p · n · m) worst case, where `p` is the number of patterns, `n = len(word)`, and `m` is the average pattern length (CPython uses a tuned substring search, often closer to O(n + m) per pattern in practice).
- **Space:** O(1) beyond the inputs.

## Notes

- Given the tiny constraints, the built-in substring search is the intended solution; no need for KMP / suffix-automaton machinery.
