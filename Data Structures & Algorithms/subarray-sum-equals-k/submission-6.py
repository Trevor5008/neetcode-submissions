"""
Given an array of ints [nums] and an integer 'k'
return the total number of subarrays whose sum == k

Ex1: nums = [2,-1,1,2], k = 2 -> 4 ([2], [2,-1,1], [-1,1,2], [2])
Ex2: nums = [4,4,4,4], k = 4 -> 4 ([4],[4],[4],[4])
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        total = 0
        totalHits = 0
        for num in nums:
            total += num
            if total - k in counts:
                totalHits += counts[total - k]
            counts[total] = counts.get(total, 0) + 1
        return totalHits