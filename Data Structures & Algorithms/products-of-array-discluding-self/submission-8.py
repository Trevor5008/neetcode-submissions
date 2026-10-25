class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        postfix = 1
        for i in range(len(nums)):
            res[i] *= postfix
            postfix *= nums[i]

        prefix = 1
        for i in reversed(range(len(nums))):
            res[i] *= prefix
            prefix *= nums[i]
        
        return res