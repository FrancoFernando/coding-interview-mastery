# 3753. Total Waviness of Numbers in Range II

**Difficulty:** Hard
**Link:** [LeetCode](https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/)

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

In **version II**, the range can be very large (up to `10^15`), so brute force does not work and digit DP is required.

---

## Step 0 - Why brute force fails

For the small-input version (`num2 <= 10^5`), this works:

```python
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return sum(1
            for n in range(num1, num2 + 1)
            for s in (str(n),)
            for a, b, c in zip(s, s[1:], s[2:])
            if a < b > c or a > b < c)
```

Using `for s in (str(n),)` is an idiom for "let-binding inside a comprehension" - `str(n)` is computed once per `n`. The triple-comparison `a < b > c` is Python's chained comparison and reads exactly like the peak definition. Equal neighbors (like `1332`) correctly produce 0 because the inequalities are strict.

But for `num2 <= 10^15`, iterating every number is impossible. We need to **count without enumerating**. That points to **digit DP**.

---

## Step 1 - Range to prefix

Define `f(N)` = total waviness across all numbers in `[1, N]`.

Then:

```text
answer = f(num2) - f(num1 - 1)
```

This reduces the problem to solving one cleaner subproblem: given `N` (up to 15 digits), compute the total waviness over `[0, N]`.

---

## Step 2 - Build numbers digit by digit

Instead of listing numbers, think of building each number by filling slots left to right. For `N = 547`, every number from 0 to 547 corresponds to a way to fill 3 slots `[_, _, _]` so the result does not exceed 547.

15 slots x 10 choices each is roughly `10^15` numbers, but only ~15 decision points if we group numbers that share a prefix.

---

## Step 3 - What state do we need?

When placing a digit at position `i`, to decide if the digit at position `i-1` is a peak or valley we need the digits at positions `i-2`, `i-1`, and `i`. So at any point we only need the **last two digits placed**.

The future depends on the past *only through the last two digits*.

State: `helper(pos, prev1, prev2, tight, started)`.

- `pos` - next slot to fill (0 = leftmost)
- `prev1` - digit at `pos-1`, or `-1` if no real digit there yet
- `prev2` - digit at `pos-2`, or `-1` if not enough real digits placed
- `tight` - are we still hugging `N`'s prefix?
- `started` - have we placed a non-zero digit yet (i.e., are we past leading zeros)?

### `tight` explained

`tight = True` means **every digit placed so far matches `N`'s prefix exactly**. At the very start it is vacuously true (no digits placed yet, so no disagreement).

For `N = 547`:

| Placed so far | Tight?        | Next digit can be           |
| ------------- | ------------- | --------------------------- |
| `[]`          | True          | 0 to 5 (capped by N[0] = 5) |
| `[5]`         | True          | 0 to 4 (capped by N[1] = 4) |
| `[5, 4]`      | True          | 0 to 7 (capped by N[2] = 7) |
| `[3]`         | False (3 < 5) | 0 to 9                      |
| `[5, 2]`      | False (2 < 4) | 0 to 9                      |

Transition: `new_tight = tight and d == limit`. Once you drop strictly below the cap, you are free forever after.

If we started with `tight = False`, we would let slot 0 be 9, build `999`, and overcount. If we never tracked `tight`, the unbounded subproblems would not collapse and memoization would not help.

### `started` explained

`started` handles **leading zeros**, which exist because we represent shorter numbers using leading zeros (e.g., `47` inside `N = 547` is `[0, 4, 7]`).

If we treated the leading `0` as a real digit, we would call `4` a "middle digit" with neighbors `0` and `7` - wrong, because in `47` the digit `4` is the *first* digit and cannot be a peak.

| Placed so far         | started? | Meaning                          |
| --------------------- | -------- | -------------------------------- |
| `[]`, `[0]`, `[0, 0]` | False    | still in leading zeros           |
| `[0, 4]`              | True     | this is the 2-digit number 4_    |
| `[3]`                 | True     | a 3-digit number starting with 3 |

Transition: `new_started = started or d > 0`.

While `started = False`, we keep `prev1 = prev2 = -1` so that peak/valley checks naturally never fire.

---

## Step 4 - Return TWO values

A common trap: returning just a count. But we want a **sum of waviness**, not a count.

`helper` returns `(cnt, wav)`:

- `cnt` - how many valid numbers can be formed from this state
- `wav` - total waviness across all those numbers

Why both? When you place a digit and that finalizes a peak at the previous position, that peak contributes `+1` to **every** completion. So the contribution to `wav` is `1 x cnt_of_completions`. You need the count to scale the contribution.

---

## Step 5 - The transition and the `extra` term

At each call, loop `d` from `0` to `(N[pos] if tight else 9)`:

1. Recursively compute `(c, w)` for the next position.
2. Decide whether placing `d` makes `prev1` a peak or valley.
3. Accumulate.

**Why `extra = c`?** When `prev1` is a peak (`prev2 < prev1 > d`), every one of the `c` completions of the remaining slots produces a different full number - but in **all** of them, `prev1` is still a peak (peaks only depend on `prev2`, `prev1`, `d`, which are already locked in). So that single decision contributes `1 x c = c` to the total waviness.

Example: `pos = 2`, `prev2 = 1`, `prev1 = 5`, `d = 3`, one slot remaining.

- `1 < 5 > 3` -> peak. Remaining slot can be 0-9, so `c = 10`.
- Completions: `1530, 1531, ..., 1539`.
- In every one, the `5` at position 1 is a peak.
- Contribution: `10`.

**Guard**: only check peak/valley when `prev2 != -1`. That condition means we have placed at least two real digits, and we are now placing the third - the earliest moment a peak/valley judgment is meaningful. (The check also implicitly requires `started`, since `prev2` can only be set after `started` flips to True.)

Each step locks in **at most one** peak/valley (the one centered at `prev1`). Peaks further left were already counted on earlier steps; peaks further right will be counted later. That is the accounting trick.

---

## Step 6 - Base case

When `pos == slots`, return `(1, 0)`. We finished building one number, and any peaks/valleys it contains were counted at the moment they got their right neighbor.

---

## Step 7 - Memoization

State space: `pos (~16) x prev1 (11) x prev2 (11) x tight (2) x started (2)` is roughly 7,800 entries, each doing 10 transitions. Effectively instant. `@cache` is enough.

The cache is re-created for each call to `solve(num)` because `digits` (the upper bound) changes between `solve(num2)` and `solve(num1 - 1)`.

---

## Solution

```python
from functools import cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(num: int) -> int:
            digits = str(num)
            slots = len(digits)

            @cache
            def helper(pos, prev1, prev2, tight, started):
                if pos == slots:
                    return (1, 0)
                limit = int(digits[pos]) if tight else 9
                cnt, wav = 0, 0
                for d in range(limit + 1):
                    new_started = started or d > 0
                    new_prev1 = d if new_started else -1
                    new_tight = tight and d == limit
                    c, w = helper(pos + 1, new_prev1, prev1, new_tight, new_started)
                    extra_w = 0
                    if prev2 != -1:
                        if prev2 < prev1 > d or prev2 > prev1 < d:
                            extra_w = c
                    cnt += c
                    wav += w + extra_w
                return (cnt, wav)

            return helper(0, -1, -1, True, False)[1]

        return solve(num2) - solve(num1 - 1)
```

### Correctness check on the example

`num1 = 120, num2 = 130`:

- `solve(130) = 12`. Waviness across 0-130:
  - 101-109: nine valleys (`1 > 0 < d` for d > 0).
  - 120, 121: two peaks (`1 < 2 > 0` and `1 < 2 > 1`).
  - 130: one peak (`1 < 3 > 0`).
  - Total = 12.
- `solve(119) = 9` (just 101-109).
- Answer = 12 - 9 = 3.

### Edge cases

- `num1 = 1` -> `solve(0)`. With `num = 0`, `digits = "0"`, the only valid number is 0 itself, returning `(1, 0)`. Subtracting 0 is harmless.
- Numbers with equal adjacent digits (e.g., `1332`) have waviness 0 - the strict inequality in `prev2 < prev1 > d` and `prev2 > prev1 < d` (Python's chained comparisons) handles this automatically.

---

## Complexity

- **Time:** `O(L * |prev1| * |prev2| * 2 * 2 * 10)` where `L` is the number of digits in `N`. For `N <= 10^15`, this is about `15 * 11 * 11 * 40` is roughly 73k operations per call to `solve`. We call `solve` twice. Effectively instant.
- **Space:** `O(L * |prev1| * |prev2|)` for the memoization cache - a few thousand entries.

## Notes

- Digit DP pattern: **prefix split** -> **build digit by digit** -> **state = last few digits + (tight, started)** -> **memoize**.
- The "return `(cnt, sum)`" idea generalizes to any digit DP that sums a property (digit sum, number of specific digits, etc.) rather than just counting numbers.
- When debugging digit DP, always compare against a brute force on a small range. The brute force from Step 0 is the perfect oracle for `num2 <= 10^5`.
