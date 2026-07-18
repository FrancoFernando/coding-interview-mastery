# 1979. Find Greatest Common Divisor of Array

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

## Problem Description

Return the greatest common divisor of the **smallest** and **largest** numbers in `nums`.

## Approach

Find `min` and `max` in one pass each, then take their GCD. `math.gcd` is exactly the requested operation and runs the Euclidean algorithm:

```python
return gcd(min(nums), max(nums))
```

## Complexity

- **Time:** O(n) to scan for min/max, plus O(log(min·max)) for the GCD.
- **Space:** O(1).

## Notes

- `math.gcd` *is* the greatest-common-divisor function, so using it expresses intent directly (under the hood: Euclid's algorithm).
- Manual fallback if `gcd` weren't available — scan divisors downward from `min` and return the first that divides both:
  ```python
  lo, hi = min(nums), max(nums)
  for d in range(lo, 0, -1):
      if lo % d == 0 and hi % d == 0:
          return d
  ```
  Correct but O(min) instead of O(log). Iterating downward and returning on the first hit stops as soon as the largest common divisor is found.
