class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        runSum = 0
        for i in range(len(nums)):
            runSum += nums[i]
            if (runSum - nums[i]) * 2 == total - nums[i]:
                return i
        return -1