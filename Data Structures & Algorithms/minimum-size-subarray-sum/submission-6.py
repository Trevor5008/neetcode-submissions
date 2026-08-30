"""
Given an array of positive inteers 'nums' and a positive int 'target'
return the minimum length of a subarray whose sum is >= target
If none exists, return 0

Ex1: target = 10, nums = [2,1,5,1,5,3] -> 3 (5,1,5)
Ex2: target = 5, nums = [1,2,1] -> 0
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = sum(nums)
        if total < target: return 0
        bestRange = len(nums)
        currSum = 0
        l = 0
        for r in range(bestRange):
            currSum += nums[r]
            if currSum >= target:
                bestRange = min(bestRange, r - l + 1)
            while currSum > target and l <= r:
                currSum -= nums[l] 
                l += 1
                if currSum >= target:
                    bestRange = min(bestRange, r - l + 1)
        return bestRange if bestRange > 0 else 0

        