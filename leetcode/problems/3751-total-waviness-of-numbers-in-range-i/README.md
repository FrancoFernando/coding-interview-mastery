# 3751. Total Waviness of Numbers in Range I

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/)

## Problem Description

You are given two integers `num1` and `num2` representing an inclusive range `[num1, num2]`.

The **waviness** of a number is the total count of its peaks and valleys:

- A digit is a **peak** if it is strictly greater than both immediate neighbors.
- A digit is a **valley** if it is strictly less than both immediate neighbors.
- The first and last digits of a number cannot be peaks or valleys.
- Any number with fewer than 3 digits has waviness 0.

Return the total sum of waviness for all numbers in `[num1, num2]`.

### Example

```text
Input:  num1 = 120, num2 = 130
Output: 3

In the range [120, 130]:
  120: middle digit 2 is a peak (1 < 2 > 0) -> waviness 1
  121: middle digit 2 is a peak (1 < 2 > 1) -> waviness 1
  130: middle digit 3 is a peak (1 < 3 > 0) -> waviness 1
Everything else has waviness 0. Total = 3.
```

This is **version I**: `1 <= num1 <= num2 <= 10^5`, so brute force is fine. For version II (`10^15`) see [3753](../3753-total-waviness-of-numbers-in-range-ii/).

---

## Approach

With at most `10^5` numbers, each at most 6 digits, you can iterate every number and check every triple of consecutive digits. Total work is well under a million operations.

### Step 1 - Reduce to a per-number helper

```python
total = sum(waviness(n) for n in range(num1, num2 + 1))
```

The real question is: how do you compute `waviness(n)` Pythonically?

### Step 2 - Get the digits

Convert `n` to a string. Now you have a sequence of characters you can compare directly. For single digits, `'3' > '2'` lexicographically matches the numeric comparison, so there is no need to convert each character back to `int`.

### Step 3 - Slide a window of 3

For each triple of consecutive digits `(a, b, c)`, `b` counts when:

- `a < b > c` (peak), or
- `a > b < c` (valley).

Idiomatic sliding window of 3: `zip(s, s[1:], s[2:])`.

### Step 4 - Count with `sum`

```python
sum(1 for a, b, c in zip(s, s[1:], s[2:]) if a < b > c or a > b < c)
```

`a < b > c` is Python's **chained comparison** - reads exactly like the problem statement, and the strict inequalities naturally make equal neighbors (e.g. the two `3`s in `1332`) not count as peaks or valleys.

---

## Solution

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum(1
            for n in range(num1, num2 + 1)
            for s in (str(n),)
            for a, b, c in zip(s, s[1:], s[2:])
            if a < b > c or a > b < c)
```

### Why `for s in (str(n),)`?

A common pitfall is writing the inner loop as `for a, b, c in zip(str(n), str(n)[1:], str(n)[2:])`, which calls `str(n)` three times per number. The idiom `for s in (str(n),)` is a **let-binding inside a comprehension**: it iterates a one-element tuple containing `str(n)`, computed once, and gives the rest of the comprehension a name `s` to reuse.

Equivalent, more readable form using a helper:

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(n: int) -> int:
            s = str(n)
            return sum(1 for a, b, c in zip(s, s[1:], s[2:])
                       if a < b > c or a > b < c)
        return sum(waviness(n) for n in range(num1, num2 + 1))
```

Both are equally fast. The one-liner is more compact; the helper version is easier to debug.

### Edge cases

- Numbers with fewer than 3 digits: `zip(s, s[1:], s[2:])` produces an empty iterator, so they contribute 0 automatically.
- Equal adjacent digits (e.g. `1332`): the strict `<` and `>` in the chained comparison correctly produce 0.

---

## Complexity

- **Time:** `O((num2 - num1 + 1) * D)` where `D` is the number of digits (<= 6 for the constraints). For `num2 = 10^5`, roughly `6 * 10^5` operations.
- **Space:** `O(D)` for each `str(n)`. No persistent allocation.

## Notes

- Same problem, larger range: [3753 - Total Waviness of Numbers in Range II](../3753-total-waviness-of-numbers-in-range-ii/) uses digit DP.
- The `for var in (expr,)` trick is a useful idiom in any nested comprehension where you'd otherwise recompute the same value multiple times.
