class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        nums = sorted(nums)
        el = nums[0]
        for i in range(1, len(nums)):
            if el == nums[i]:
                return True
            el = nums[i]
        return False