class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap: int) -> bool:
            days_needed = 1
            curr_weight = 0

            for w in weights:
                if curr_weight + w > cap:
                    days_needed += 1
                    curr_weight = 0
                curr_weight += w
            return days_needed <= days

        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res