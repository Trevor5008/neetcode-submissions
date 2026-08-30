class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minPrice, maxProfit = prices[0], 0
        for price in prices:
            minPrice = min(price, minPrice)
            currProfit = price - minPrice
            maxProfit = max(currProfit, maxProfit)
        return maxProfit
