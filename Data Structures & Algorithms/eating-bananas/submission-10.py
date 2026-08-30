class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/mid)
            if hrs <= h:
                r = mid - 1
                res = min(res, mid)
            else:
                l = mid + 1
        return res