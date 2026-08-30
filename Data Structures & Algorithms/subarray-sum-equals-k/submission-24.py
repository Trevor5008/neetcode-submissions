class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts, currSum, total = {0:1}, 0, 0
        for i in range(len(nums)):
            currSum += nums[i]
            total += counts.get(currSum - k, 0)
            counts[currSum] = counts.get(currSum, 0) + 1
        return total