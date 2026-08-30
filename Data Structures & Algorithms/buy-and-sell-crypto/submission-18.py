class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxProfit = 0
        for price in prices:
            if price < buy:
                buy = price
            currProfit = price - buy
            maxProfit = max(maxProfit, currProfit)
        return maxProfit
