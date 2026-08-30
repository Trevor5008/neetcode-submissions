"""
Given an integer array 'piles' where piles[i] is the # of bananas in the ith pile
also, given an integer 'h', which represents the # of hours to eat all bananas

return the minimum int 'k' such that you can eat all the bananas w/in 'h' hours

Ex1: piles = [1,4,3,2], h = 9 -> 2 (takes 2 bananas/hr to finish in 9 hours)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # minimimum rate is 1/hr, max is biggest pile

        res = r
        while l <= r:
            mid = (r + l) // 2
            hours_spent = 0
            for p in piles:
                hours_spent += math.ceil(p / mid)
            
            if hours_spent <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res