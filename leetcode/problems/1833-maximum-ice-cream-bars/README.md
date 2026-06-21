# 1833. Maximum Ice Cream Bars

**Difficulty:** Medium
**Link:** [LeetCode](https://leetcode.com/problems/maximum-ice-cream-bars/)

## Problem Description

You are given an array `costs` where `costs[i]` is the price of the i-th ice cream bar in coins, and an integer `coins` representing your budget. Return the maximum number of ice cream bars you can buy.

## Approach

Greedy: always buy the cheapest available bar first. Each cheap bar removed leaves more budget for additional bars, so this can never be worse than skipping it for a more expensive option.

Two ways to realize the greedy:

1. **Sort + linear scan** — O(N log N).
2. **Counting sort** — O(N + max_cost), exploited here because LeetCode constrains `costs[i] ≤ 10^5`.

The counting-sort variant builds a `freq` array indexed by cost, then walks costs from 1 upward. For each price bucket, compute in O(1) how many bars are affordable (`min(freq[cost], coins // cost)`), buy them in bulk, and stop as soon as `coins < cost` (no larger price is reachable either).

## Complexity

- **Time:** O(N + max_cost). Building `freq` is O(N); the price scan is O(max_cost).
- **Space:** O(max_cost) for the frequency array.

## Notes

- Iterate from `cost = 1` rather than `0`: the problem guarantees `costs[i] ≥ 1`, so index 0 is unused, and starting at 1 sidesteps the `coins // 0` trap if the constraint ever changes.
- Bulk math (`buyable = min(freq[cost], coins // cost)`) avoids an inner loop that would otherwise decrement `coins` one purchase at a time — same asymptotic cost, smaller constant.
- The `if coins < cost: break` early exit matters because subsequent costs only grow; without it, the loop spins through empty buckets all the way to `max_cost`.
- The standard `costs.sort()` + linear scan is more compact and has no `max_cost` dependency. Prefer it when item prices can be very large.
