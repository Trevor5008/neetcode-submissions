from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            rate = (l + r) // 2
            hours = 0
            # rate = bananas / hour -> bananas = rate / hr
            for pile in piles:
                hours += ceil(pile / rate)
            print(hours)
            if hours > h:
                l = rate + 1
            else:
                best = min(best, rate)
                r = rate - 1
        return best