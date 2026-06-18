"""
LeetCode #1344: Angle Between Hands of a Clock
Difficulty: Medium
Link: https://leetcode.com/problems/angle-between-hands-of-a-clock/
"""

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Minute hand: 360 / 60 = 6 degrees per minute.
        minute_deg = minutes * 6
        # Hour hand: 360 / 12 = 30 degrees per hour, plus 0.5 deg per minute of drift.
        # hour % 12 maps 12 o'clock back to 0.
        hour_deg = (hour % 12) * 30 + minutes * 0.5
        diff = abs(hour_deg - minute_deg)
        # The two hands form two angles summing to 360; return the smaller one.
        return min(diff, 360 - diff)

def test_solution():
    sol = Solution()
    assert abs(sol.angleClock(12, 30) - 165.0) < 1e-5
    assert abs(sol.angleClock(3, 30) - 75.0) < 1e-5
    assert abs(sol.angleClock(3, 15) - 7.5) < 1e-5
    assert abs(sol.angleClock(4, 50) - 155.0) < 1e-5
    assert abs(sol.angleClock(12, 0) - 0.0) < 1e-5
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
