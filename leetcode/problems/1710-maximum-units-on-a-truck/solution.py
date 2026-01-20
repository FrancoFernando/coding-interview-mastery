"""
LeetCode #1710: Maximum Units on a Truck
Difficulty: Easy
Link: https://leetcode.com/problems/maximum-units-on-a-truck/
"""
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort by units per box in descending order
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        total_units = 0
        remaining_capacity = truckSize

        for num_boxes, units_per_box in boxTypes:
            # Take as many boxes of this type as possible
            boxes_to_take = min(num_boxes, remaining_capacity)
            total_units += boxes_to_take * units_per_box
            remaining_capacity -= boxes_to_take

            if remaining_capacity == 0:
                break

        return total_units
