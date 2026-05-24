// Last updated: 24/05/2026, 15:00:47
1class Solution {
2    public int maxProfit(int[] prices) {
3        int maxProfit = 0;
4        int left = 0;
5
6        for (int right = 0; right < prices.length; right++) {
7            if (prices[right] < prices[left]) {
8                left = right;
9            } else {
10                maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
11            }
12        }
13
14        return maxProfit;
15    }
16}