/*
LeetCode #70: Climbing Stairs
Difficulty: Easy
Link: https://leetcode.com/problems/climbing-stairs/
*/

public class Solution {
    public int ClimbStairs(int n) {

        if (n <= 2) return n;

        int oneStepBefore = 2;
        int twoStepsBefore = 1;

        for (int i = 3; i <=n; i++) {
            int tmp = oneStepBefore;
            oneStepBefore += twoStepsBefore;
            twoStepsBefore = tmp;
        }
        return oneStepBefore;
    }
}
