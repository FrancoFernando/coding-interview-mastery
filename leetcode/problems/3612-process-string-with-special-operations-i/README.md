# 3612. Process String with Special Operations I

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/process-string-with-special-operations-i/)

## Problem Description

You are given a string `s` consisting of lowercase English letters and the special characters `*`, `#`, and `%`. Build a new string `result` by processing `s` left-to-right:

- A lowercase letter is appended to `result`.
- `*` removes the last character from `result` (if any).
- `#` duplicates `result` (`result = result + result`).
- `%` reverses `result`.

Return the final `result`.

### Example

```text
Input:  s = "a#b%*"
Output: "ba"

i  s[i]  Operation             Current result
0  'a'   Append 'a'            "a"
1  '#'   Duplicate result      "aa"
2  'b'   Append 'b'            "aab"
3  '%'   Reverse result        "baa"
4  '*'   Remove last character "ba"
```

This is **version I**. A future "II" tightens constraints so that `#` operations would blow up the materialized string and force a lazy approach.

---

## Approach

This is a straight **simulation problem**. Walk through `s` once, mutate a buffer per character. The only real design choice is the buffer.

### Step 1 - Pick the buffer

Look at each op's cost requirement:

| Op     | Need                  |
| ------ | --------------------- |
| letter | O(1) append to end    |
| `*`    | O(1) pop from end     |
| `#`    | read all + append all |
| `%`    | reverse in place      |

A Python **list of characters** gives O(1) for the first two and clean primitives (`*= 2`, `.reverse()`) for the other two. A Python `str` would work but is immutable, so every op would rebuild — wasted work.

### Step 2 - Handle each operation

- **letter** -> `result.append(c)`
- **`*`** -> guard the empty case: `elif c == "*" and result:`. The spec says "if it exists", so popping an empty list should silently no-op.
- **`#`** -> `result *= 2`. Idiomatic and equivalent to `result = result + result`. Watch out in other languages: extending a list with itself while iterating can be a trap.
- **`%`** -> `result.reverse()` in place. O(n).

### Step 3 - Join at the end

`''.join(result)` is the canonical O(n) build. Building the string char-by-char inside the loop would be O(n^2).

### Trace `"a#b%*"`

```text
[]  ->  a: [a]  ->  #: [a,a]  ->  b: [a,a,b]  ->  %: [b,a,a]  ->  *: [b,a]  ->  "ba"
```

Matches the expected output.

---

## Solution

```python
class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.islower():
                result.append(c)
            elif c == "*" and result:
                result.pop()
            elif c == "#":
                result *= 2
            elif c == "%":
                result.reverse()
        return ''.join(result)
```

### Notes on style

- `result` (vs `len(result) > 0`) leans on Python's truthiness — an empty list is falsy.
- `result *= 2` is a clean rewrite of `result.extend(result[:])`. Both are safe; `*= 2` is terser.
- `c.islower()` is a defensive catch-all for "any other letter" — switching it to a plain `else` is fine given the constraints, slightly faster, slightly less defensive.

---

## Complexity

- **Time:** O(N * M) worst case, where N = len(s) and M = max length of `result`. `#` and `%` each cost O(M), and repeated `#`s can grow M exponentially. Safe at the constraints of version I.
- **Space:** O(M) for the buffer.

## Notes

- The follow-up "II" will likely require **lazy evaluation**: instead of materializing `result`, track the sequence of operations and answer "what character is at index k?" in O(log N) per query. Repeated `#` makes naive simulation explode (10 `#`s in a row -> 1024x).
- Key takeaway: when ops include append + pop + reverse + duplicate, reach for a list/stack and join once at the end.
