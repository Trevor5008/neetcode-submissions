class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        currSum = 0
        res = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum - k in prefixSums:
                res += prefixSums[currSum - k]
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        return res