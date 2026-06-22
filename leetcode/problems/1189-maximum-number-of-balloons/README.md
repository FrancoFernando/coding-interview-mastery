# 1189. Maximum Number of Balloons

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/)

## Problem Description

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

## Approach

Count the characters available in `text` and the characters needed for one `"balloon"`.
For each needed character, `available[char] // count` is how many balloons that single
character can support. The limiting character — the minimum across all of them — is the
answer. Using `Counter` for `available` means missing characters lookup as `0`, so a
missing letter correctly yields `0`.

## Complexity

- **Time Complexity:** O(N) to count the characters in text
- **Space Complexity:** O(1) - the counters hold at most a fixed alphabet
