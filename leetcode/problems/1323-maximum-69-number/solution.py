"""
LeetCode #1323: Maximum 69 Number
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-69-number/
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        # Convert to string, replace first '6' with '9'
        return int(str(num).replace('6', '9', 1))
