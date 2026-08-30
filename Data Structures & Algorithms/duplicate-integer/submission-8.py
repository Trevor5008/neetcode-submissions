class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valsMap = {}
        for i in range(len(nums)):
            if nums[i] in valsMap:
                return True
            valsMap[nums[i]] = i
        return False