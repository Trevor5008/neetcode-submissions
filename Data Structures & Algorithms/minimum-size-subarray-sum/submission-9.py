"""
Given an array of positive inteers 'nums' and a positive int 'target'
return the minimum length of a subarray whose sum is >= target
If none exists, return 0

Ex1: target = 10, nums = [2,1,5,1,5,3] -> 3 (5,1,5)
Ex2: target = 5, nums = [1,2,1] -> 0
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        res = n + 1
        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                curSum = prefixSum[mid + 1] - prefixSum[i]
                if curSum >= target:
                    r = mid
                else:
                    l = mid + 1
            if l != n:
                res = min(res, l - i + 1)

        return res % (n + 1)
        