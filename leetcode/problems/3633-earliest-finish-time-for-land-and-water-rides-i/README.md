# 3633. Earliest Finish Time for Land and Water Rides I

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/)

## Problem Description

There are two categories of theme park attractions: **land rides** and **water rides**.

- `landStartTime[i]` - the earliest time the `i`th land ride can be boarded.
- `landDuration[i]` - how long the `i`th land ride lasts.
- `waterStartTime[j]` - the earliest time the `j`th water ride can be boarded.
- `waterDuration[j]` - how long the `j`th water ride lasts.

A tourist must experience **exactly one ride from each category**, in either order.

- A ride can start at its opening time or any later moment.
- A ride started at time `t` finishes at `t + duration`.
- Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the earliest possible time at which the tourist can finish both rides.

### Example

```text
landStartTime  = [2, 8]
landDuration   = [4, 1]
waterStartTime = [6]
waterDuration  = [3]
Output: 9

Pair land ride 0 (open at 2, lasts 4) with water ride 0 (open at 6, lasts 3).
Do land first: finish land at 2 + 4 = 6, water is open at 6, finish at 6 + 3 = 9.
No pairing or order finishes earlier.
```

This is **version I**, with small arrays (`1 <= n, m <= 100`), so a brute-force pass over every pair is fine. For the linear-time version see [3635](../3635-earliest-finish-time-for-land-and-water-rides-ii/).

---

## Approach

### Step 1 - Solve the single-pair case first

Forget the arrays. Given **one** land ride and **one** water ride, how early can you finish?

You have two choices of order. Let `landFinish = landStart + landDuration` and `waterFinish = waterStart + waterDuration`.

- **Land then water:** `max(landFinish, waterStart) + waterDuration`
- **Water then land:** `max(waterFinish, landStart) + landDuration`

The `max` captures "you may have to wait until the second ride opens." The single-pair answer is the smaller of the two.

### Step 2 - Try every pair

With `n, m <= 100`, there are at most `10,000` pairs. Compute the single-pair answer for each and keep the minimum. `itertools.product` gives a clean cartesian product over the two lists.

### Step 3 - Make it Pythonic

Precompute the finish times once with `zip`, then iterate pairs:

```python
landFinish  = [s + d for s, d in zip(landStartTime, landDuration)]
waterFinish = [s + d for s, d in zip(waterStartTime, waterDuration)]
```

Each element of `product` is a `(land, water)` triple-pair you can unpack directly into `(land_start, land_duration, land_finish)` and `(water_start, water_duration, water_finish)`.

---

## Solution

```python
from itertools import product


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int],
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        landFinish = [s + d for s, d in zip(landStartTime, landDuration)]
        waterFinish = [s + d for s, d in zip(waterStartTime, waterDuration)]

        return min(
            min(
                max(land_finish, water_start) + water_duration,
                max(water_finish, land_start) + land_duration,
            )
            for (land_start, land_duration, land_finish), \
                (water_start, water_duration, water_finish) in product(
                    zip(landStartTime, landDuration, landFinish),
                    zip(waterStartTime, waterDuration, waterFinish),
                )
        )
```

### Edge cases

- **Second ride already open** when the first finishes: the `max` collapses to the finish time, so no waiting is added.
- **Single ride in a category:** `product` still works with a one-element iterable.

---

## Complexity

- **Time:** `O(n * m)` for the cartesian product over the two lists.
- **Space:** `O(n + m)` for the precomputed finish-time lists.

## Notes

- The key realization is that the whole problem reduces to the **single-pair, two-order** formula; the arrays just add a search over pairs.
- Same problem, larger constraints: [3635 - Earliest Finish Time for Land and Water Rides II](../3635-earliest-finish-time-for-land-and-water-rides-ii/) drops this to `O(n + m)` by observing you only ever want the ride with the **minimum finish time** as the first ride.
