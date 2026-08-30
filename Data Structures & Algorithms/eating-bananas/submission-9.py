class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            print(f"Total hours {hours} to eat {sum(piles)} bananas")
            if hours > h:
                l = mid + 1
            elif hours <= h:
                r = mid - 1
                best = min(best, mid)
        return best
            