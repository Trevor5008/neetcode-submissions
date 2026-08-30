"""
Given an array of positive integers 'nums' and a positive integer 'target'
return the minimal length of a subarray whose sum is >= target
return 0 if no such subarray

Ex1: target = 10, nums = [2,1,5,1,5,3] -> 3 ([5,1,5])
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        res = len(nums)

        l = 0
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l += 1
        return res
            
