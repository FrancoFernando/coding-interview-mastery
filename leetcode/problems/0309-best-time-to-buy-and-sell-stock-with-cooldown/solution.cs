/*
LeetCode #309: Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
*/

public class Solution {

   private Dictionary<(int, bool), int> memo;

    public int MaxProfit(int[] prices) {
        memo = new Dictionary<(int, bool), int>();
        return Dfs(prices, 0, true);
    }

    private int Dfs(int[] prices, int day, bool canBuy) {

        if (day >= prices.Length) {
            return 0;
        }

        if (memo.ContainsKey((day,canBuy))) {
            return memo[(day,canBuy)];
        }

        int doNothing = Dfs(prices, day+1, canBuy);
        int sellOrBuy;
        if (canBuy) {
            sellOrBuy = Dfs(prices, day+1, false) - prices[day];
        }
        else {
            sellOrBuy = Dfs(prices, day+2, true) + prices[day];
        }

        int maxProfit = Math.Max(doNothing, sellOrBuy);
        memo[(day,canBuy)] = maxProfit;
        return maxProfit;
    }
}
