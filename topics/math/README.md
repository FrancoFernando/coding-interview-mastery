# Math

## Overview

Math problems rely on number-theory facts, digit manipulation, and arithmetic identities rather than heavy data structures. The win is usually a formula or property that replaces a loop.

## Key Concepts

- **Digit manipulation**: peel digits with `divmod(n, 10)` (right-to-left) or via `str(n)` (left-to-right)
- **Modular arithmetic**: `(a + b) % m`, `(a * b) % m`; answers "mod 1e9+7"
- **Number theory**: GCD/LCM, primes/sieve, divisors, factorization
- **Combinatorics**: counting, permutations, combinations
- **Geometry**: angles, coordinates, distances

## Common Patterns

1. **Digit peeling** - `while n: n, d = divmod(n, 10)` to process each digit
2. **Rebuild a number** - `x = x * 10 + d` (left-to-right) or `x += d * mult; mult *= 10` (right-to-left)
3. **GCD / LCM** - `math.gcd`; `lcm = a * b // gcd(a, b)`
4. **Sieve of Eratosthenes** - all primes up to n in O(n log log n)
5. **Fast exponentiation** - `pow(base, exp, mod)` for modular powers

## Python Tips

```python
from math import gcd, isqrt

n, d = divmod(n, 10)        # quotient and last digit in one step
digits = [int(c) for c in str(n)]
result = pow(base, exp, 10**9 + 7)   # modular exponentiation
```

## Notes

[Add your study notes here]
