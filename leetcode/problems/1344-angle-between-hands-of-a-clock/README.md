# 1344. Angle Between Hands of a Clock

**Difficulty:** Medium  
**Link:** [LeetCode](https://leetcode.com/problems/angle-between-hands-of-a-clock/)

## Problem Description

Given two numbers, `hour` and `minutes`, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10^-5 of the actual value will be accepted as correct.

## Approach

Convert each hand's position to an absolute angle measured clockwise from 12 o'clock:

- **Minute hand** moves a full 360° in 60 minutes → `6°` per minute → `minutes * 6`.
- **Hour hand** moves 360° in 12 hours → `30°` per hour, and also drifts `0.5°` per minute (30° / 60 min). Use `hour % 12` so that 12 o'clock maps back to 0 → `(hour % 12) * 30 + minutes * 0.5`.

Take the absolute difference. The two hands split the clock into two angles that sum to 360°, so the answer is `min(diff, 360 - diff)`.

## Complexity

- **Time Complexity:** O(1)
- **Space Complexity:** O(1)

## Notes

`hour % 12` is cleaner than a special-case `if hour == 12` and handles the wrap for free.
