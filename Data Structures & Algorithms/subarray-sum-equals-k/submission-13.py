class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0:1}
        count = 0
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            count += sums.get(currSum - k, 0)
            sums[currSum] = sums.get(currSum, 0) + 1
        return count