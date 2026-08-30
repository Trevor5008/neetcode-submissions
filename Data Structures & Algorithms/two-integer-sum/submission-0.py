class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            right = i + 1
            diff = target - nums[i]
            while right < len(nums):
                if nums[right] == diff:
                    return [i, right]
                right += 1
        return False