"""
LeetCode #1665: Minimum Initial Energy to Finish Tasks
Difficulty: Hard
Link: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
"""

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key= lambda x : x[0]-x[1])
        energy_have, energy_needed = 0, 0
        for actual, minimum in tasks:
            gap = minimum - energy_have
            if gap > 0:  
                energy_needed += gap
                energy_have += gap
            energy_have -= actual
        return energy_needed

def test_solution():
    sol = Solution()
    print("Add your tests here")

if __name__ == "__main__":
    test_solution()
