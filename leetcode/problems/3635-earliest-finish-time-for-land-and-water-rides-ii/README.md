# 3635. Earliest Finish Time for Land and Water Rides II

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/)

## Problem Description

Identical to [3633](../3633-earliest-finish-time-for-land-and-water-rides-i/), but with **large arrays** (`n, m` up to `5 * 10^4`), so the `O(n * m)` brute force over every pair is too slow.

There are two categories of theme park attractions: **land rides** and **water rides**.

- `landStartTime[i]` / `landDuration[i]` - opening time and length of the `i`th land ride.
- `waterStartTime[j]` / `waterDuration[j]` - opening time and length of the `j`th water ride.

A tourist must experience **exactly one ride from each category**, in either order. A ride started at time `t` finishes at `t + duration`; the tourist may board the second ride as soon as it is open. Return the earliest possible finish time of both rides.

---

## Approach

### Step 1 - Split by order

Group all choices into two independent subproblems and take the min of their answers:

1. Best finish going **land -> water**
2. Best finish going **water -> land**

For subproblem 1, the finish is:

```text
finish = max(landFinish[i], waterStart[j]) + waterDuration[j]
```

### Step 2 - The key observation

For a **fixed** water ride `j`, which land ride `i` do you want?

The land ride appears only inside `max(landFinish[i], ...)`. Since `max` is monotonic in `landFinish[i]`, a smaller `landFinish[i]` is **never worse** - and this is true *regardless of which `j` you picked*.

So you don't search land rides at all. You only need the **single land ride with the minimum finish time**:

```text
minLandFinish = min over i of (landStart[i] + landDuration[i])
```

Then sweep the water rides once. Symmetrically for water -> land.

> Careful: a tempting shortcut is to just pair the min-finish land ride with the min-finish water ride. That's **wrong** - the second ride's own start time matters via the `max`, so you must still sweep all of the second category.

### Step 3 - Factor the two symmetric halves

Both orders share the same shape. A small helper `best(first, second)` computes the min finish when riding `first` then `second`, and the answer is the min over both directions.

---

## Solution

```python
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        def best(first_start, first_dur, second_start, second_dur):
            first_finish = min(s + d for s, d in zip(first_start, first_dur))
            return min(max(first_finish, s) + d for s, d in zip(second_start, second_dur))

        return min(
            best(landStartTime, landDuration, waterStartTime, waterDuration),
            best(waterStartTime, waterDuration, landStartTime, landDuration),
        )
```

### Edge cases

- **Second ride already open** when the first finishes: the `max` collapses to `first_finish`, adding no wait.
- The helper is called once per direction, so each ride list is scanned at most twice total.

---

## Complexity

- **Time:** `O(n + m)` - two passes over each list (one to find the min finish, one to sweep the other category).
- **Space:** `O(1)` extra, beyond the input.

## Notes

- This is the optimized counterpart of the brute force in [3633](../3633-earliest-finish-time-for-land-and-water-rides-i/). The whole speedup comes from the monotonicity argument: the first ride should always be the one that **finishes earliest**.
- The two-direction `min` mirrors the two-order `min` of the single-pair formula - the helper just hoists "the best first ride is fixed" out of the inner loop.
