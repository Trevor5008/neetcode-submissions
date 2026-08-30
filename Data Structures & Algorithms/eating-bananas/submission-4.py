class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        bestRate = right
        while left <= right:
            mid = (left + right) // 2
            totalHrs = 0
            for p in piles:
                totalHrs += math.ceil(p/mid)
            if totalHrs > h:
                left = mid + 1
            else:
                right = mid - 1
                bestRate = mid
        return bestRate