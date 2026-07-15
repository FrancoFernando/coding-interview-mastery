# 3658. GCD of Odd and Even Sums

**Difficulty:** Easy
**Link:** [LeetCode](https://leetcode.com/problems/gcd-of-odd-and-even-sums/)

## Problem Description

Given `n`, compute `gcd(sumOdd, sumEven)` where `sumOdd` is the sum of the smallest `n` positive odd numbers and `sumEven` the sum of the smallest `n` positive even numbers.

## Approach

Use the two closed-form sums:

- Sum of the first `n` odd numbers: `1 + 3 + … + (2n-1) = n²`.
- Sum of the first `n` even numbers: `2 + 4 + … + 2n = 2·(n(n+1)/2) = n(n+1)`.

Then:

```
gcd(n², n(n+1)) = n · gcd(n, n+1) = n · 1 = n
```

because consecutive integers `n` and `n+1` are always coprime. **The answer is simply `n`.**

The solution computes the two sums and calls `math.gcd` — obviously correct at a glance and still O(1) — while the derivation shows it always reduces to `n`.

```python
sum_odd = n * n
sum_even = n * (n + 1)
return gcd(sum_odd, sum_even)
```

## Complexity

- **Time:** O(1).
- **Space:** O(1).

## Notes

- The one-liner `return n` is equally correct; the `math.gcd` form is kept for readability and to make the result self-evidently right.
- Key fact reused elsewhere: `gcd(k, k+1) = 1` for any integer `k` (consecutive integers are coprime).
