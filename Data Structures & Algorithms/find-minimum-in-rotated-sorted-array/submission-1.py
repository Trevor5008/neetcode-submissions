class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min:
                return nums[i]
        return min