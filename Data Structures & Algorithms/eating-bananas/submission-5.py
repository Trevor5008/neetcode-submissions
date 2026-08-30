class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        left, right = 1, max(piles)
        bestRate = right

        while left <= right:
            rate = (left + right) // 2
            totalHrs = 0
            for p in piles:
                totalHrs += math.ceil(p / rate)
            
            if totalHrs > h:
                left = rate + 1
            elif totalHrs <= h:
                right = rate - 1
                bestRate = min(bestRate, rate)
        return bestRate