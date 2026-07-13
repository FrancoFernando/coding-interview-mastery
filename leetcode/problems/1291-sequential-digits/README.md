# 1291. Sequential Digits

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/sequential-digits/)

## Problem Description

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:

Input: low = 100, high = 300
Output: [123,234]

Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]

Constraints:

10 <= low <= high <= 10^9

## Approach

A number has sequential digits exactly when it is a **contiguous slice of the string
`"123456789"`** — "each digit is one more than the previous" is the definition of such a
substring. Since digits can't wrap past 9, the entire universe is tiny: 8 + 7 + ... + 1 =
**36 numbers** (all substrings of length >= 2).

So there is no search to do — enumerate every substring of length 2..9, convert to an int,
and keep the ones inside `[low, high]`. Generate the string slice, compare as an integer.

Generating by increasing length, then left-to-right, yields the results already in sorted
order (every L-digit sequential number is smaller than every (L+1)-digit one), so no final
sort is needed.

## Complexity

- **Time Complexity:** O(1) — at most 36 candidates are ever examined, independent of `low`/`high`
- **Space Complexity:** O(1) — the output holds at most 36 numbers
