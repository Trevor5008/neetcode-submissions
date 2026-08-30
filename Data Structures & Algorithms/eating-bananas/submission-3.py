class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            hours_to_eat = 0
            for p in piles:
                hours_to_eat += math.ceil(p / mid)
            if hours_to_eat > h:
                l = mid + 1
            else:
                r = mid - 1
                res = min(res, mid)
        return res
