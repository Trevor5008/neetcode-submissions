"""
Given an int array 'prices' with prices at each index correspond to each day
Choose the best day to purchase and the best day to sell to maximize profit
return profit from difference (sold at - bought at)

Ex1: prices = [10, 1, 5, 6, 7, 1] -> 6 (purchase at 1, sell at 7 for profit of 6)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        
        for price in prices:
            if price < min_price:
                min_price = price
            current_profit = price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
                
        return max_profit