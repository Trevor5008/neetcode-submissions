class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights) 
        res = r
        def canShip(max_wgt):
            days_needed = 1
            current_wgt = 0
            for w in weights:
                if current_wgt + w > max_wgt:
                    days_needed += 1
                    current_wgt = 0
                current_wgt += w
            return days_needed <= days 

        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1 
            else:
                l = mid + 1
        return res