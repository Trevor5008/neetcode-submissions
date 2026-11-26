class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            rate = (l + r) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p/rate)
            if hrs <= h:
                res = min(res, rate)
                r = rate - 1
            elif hrs > h:
                l = rate + 1
        return res