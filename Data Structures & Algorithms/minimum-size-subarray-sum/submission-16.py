class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        pfxSums = {}
        currSum, l = 0, 0
        minLen = float("inf")
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLen = min(minLen, r - l + 1)
                currSum -= nums[l]
                l += 1
            pfxSums[r] = currSum
        return minLen