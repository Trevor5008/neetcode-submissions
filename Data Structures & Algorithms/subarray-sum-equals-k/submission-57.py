class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        currSum = 0
        total = 0
        for r in range(len(nums)):
            currSum += nums[r]
            total += sums.get(currSum - k, 0)
            sums[currSum] = sums.get(currSum, 0) + 1
        return total