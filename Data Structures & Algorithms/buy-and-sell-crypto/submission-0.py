

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell, max_profit = 0, 0

        for i in reversed(range(1, len(prices))):
            max_sell = max(max_sell, prices[i])
            print(max_sell)
            profit = max_sell - prices[i - 1]
            max_profit = max(profit, max_profit)
        return max_profit