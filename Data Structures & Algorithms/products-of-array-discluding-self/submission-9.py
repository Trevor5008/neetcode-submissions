class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1]*len(nums)
        prefix = 1
        for i in range(len(prods)):
            prods[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in reversed(range(len(prods))):
            prods[i] *= postfix
            postfix *= nums[i]
        return prods