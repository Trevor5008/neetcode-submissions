class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy, max_profit = prices[0], 0

        for i in range(len(prices)-1):
            min_buy = min(min_buy, prices[i])
            profit = prices[i+1] - min_buy
            max_profit = max(max_profit, profit)
        return max_profit