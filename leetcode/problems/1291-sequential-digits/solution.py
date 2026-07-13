"""
LeetCode #1291: Sequential Digits
Difficulty: Medium
Link: https://leetcode.com/problems/sequential-digits/

Idea
----
Every "sequential digits" number is a contiguous slice of "123456789" (each digit
is one more than the previous). So the entire universe is just 36 numbers -- all
substrings of length >= 2. Enumerate them and keep the ones inside [low, high].

Because we generate by increasing length, then left-to-right, the results come out
already sorted (every L-digit number is smaller than every (L+1)-digit one).

Complexity: O(1) -- at most 36 candidates regardless of low/high.
"""
from typing import List

DIGITS = "123456789"


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for length in range(2, 10):                 # low >= 10 => at least 2 digits
            for start in range(len(DIGITS) - length + 1):
                num = int(DIGITS[start : start + length])
                if low <= num <= high:
                    result.append(num)
        return result
