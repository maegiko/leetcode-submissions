// Last updated: 18/08/2026, 14:57:33
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int left = 0;

        for (int right = 0; right < prices.length; right++) {
            if (prices[right] < prices[left]) {
                left = right;
            } else {
                maxProfit = Math.max(maxProfit, prices[right] - prices[left]);
            }
        }

        return maxProfit;
    }
}