# 3867. Sum of GCD of Formed Pairs

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/)

## Problem Description

Build `prefixGcd[i] = gcd(nums[i], max(nums[0..i]))`. Sort it, repeatedly pair the smallest unpaired element with the largest unpaired element, and sum `gcd` over the pairs. If `n` is odd, the middle element is ignored.

## Approach

Faithful simulation of the three described steps.

1. **Build `prefixGcd`** in one pass with a running max:
   ```python
   mx = 0
   for x in nums:
       mx = max(mx, x)
       prefix_gcd.append(gcd(x, mx))
   ```
2. **Sort** `prefix_gcd`.
3. **Two pointers** from both ends, summing `gcd(prefix_gcd[lo], prefix_gcd[hi])`:
   ```python
   lo, hi = 0, len(prefix_gcd) - 1
   while lo < hi:
       total += gcd(prefix_gcd[lo], prefix_gcd[hi])
       lo += 1; hi -= 1
   ```

The `while lo < hi` condition handles the odd-`n` case for free: the pointers meet at the middle element (`lo == hi`), the loop stops, and that element is never paired.

## Complexity

- **Time:** O(n log n) — the sort dominates; each `gcd` is ~O(log(max value)).
- **Space:** O(n) for `prefixGcd`.

## Notes

- Don't special-case odd `n` — the two-pointer bound leaves the middle unpaired automatically.
- `mx` starting at `0` is safe: `gcd(x, 0) = x`, and the first `max(0, nums[0])` is just `nums[0]`.
- Since `mx >= nums[i]` always, `prefixGcd[i] = gcd(nums[i], mx)` is a divisor of `nums[i]`.
