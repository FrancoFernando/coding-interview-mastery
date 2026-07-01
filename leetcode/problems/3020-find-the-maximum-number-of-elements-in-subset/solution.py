"""
LeetCode #3020: Find the Maximum Number of Elements in Subset
Difficulty: Medium
Link: https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/
"""
from typing import List
from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)

        # The pattern is a palindrome ladder: x, x^2, x^4, ..., peak, ..., x^4, x^2, x.
        # Every level below the peak is used twice; the peak is used once.
        # 1 is special: 1^2 == 1, so the chain never grows. A block of ones must
        # have odd length (peak + symmetric pairs).
        max_length = count[1] if count[1] & 1 else count[1] - 1

        for base in count:
            if base == 1:
                continue

            # Climb x -> x^2 -> x^4 ... while each level has a pair to spare.
            length = 0
            val = base
            while count[val] >= 2:
                length += 2
                val = val * val

            if count[val] >= 1:
                length += 1  # val sits alone at the top -> it is the peak
            else:
                length -= 1  # can't cap here; a previous level's pair becomes the peak

            if length > max_length:
                max_length = length

        return max_length


def test_solution():
    sol = Solution()

    assert sol.maximumLength([5, 4, 1, 2, 2]) == 3
    print("Test 1 passed: [5,4,1,2,2] -> 3")

    assert sol.maximumLength([1, 3, 2, 4]) == 1
    print("Test 2 passed: [1,3,2,4] -> 1")

    assert sol.maximumLength([1, 1, 1]) == 3
    print("Test 3 passed: three ones -> 3 (odd block)")

    assert sol.maximumLength([1, 1]) == 1
    print("Test 4 passed: two ones -> 1 (even block trimmed)")

    assert sol.maximumLength([2, 4, 16, 4, 2]) == 5
    print("Test 5 passed: full chain 2,4,16,4,2 -> 5")

    assert sol.maximumLength([3, 9, 3]) == 3
    print("Test 6 passed: 3,9,3 -> 3")

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
