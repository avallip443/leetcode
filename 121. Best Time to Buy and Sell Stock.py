"""
Solution: Use sliding window - set two pointers for the buy/sell days and check if sell > buy (i.e. profitable).
- If so, update max_profit and inc sell
- Otherwise, set buy to sell (since sell has a lower price)
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(curr_profit, max_profit)
            else:
                l = r
            r += 1
        
        return max_profit
