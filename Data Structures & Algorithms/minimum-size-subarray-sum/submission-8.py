"""
Given an array of positive inteers 'nums' and a positive int 'target'
return the minimum length of a subarray whose sum is >= target
If none exists, return 0

Ex1: target = 10, nums = [2,1,5,1,5,3] -> 3 (5,1,5)
Ex2: target = 5, nums = [1,2,1] -> 0
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        res = float('inf')
        
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        
        return 0 if res == float('inf') else res

        