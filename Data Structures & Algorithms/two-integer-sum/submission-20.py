class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for l in range(len(nums)-1):
            diff = target - nums[l]
            for r in range(l + 1, len(nums)):
                if nums[r] == diff:
                    return [l, r]
        return []