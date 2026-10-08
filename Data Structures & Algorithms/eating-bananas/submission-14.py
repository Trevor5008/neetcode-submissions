class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            rate = (l + r) // 2
            # rate = piles / hr
            hours = 0
            for p in piles:
                hours += math.ceil(p / rate)
            if hours <= h:
                best = min(best, rate)
                r = rate - 1
            else:
                l = rate + 1
        return best