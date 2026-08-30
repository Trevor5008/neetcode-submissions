class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1} # 0 appears once initially
        currSum = 0
        res = 0
        for val in nums:
            currSum += val
            res += prefixSums.get(currSum - k, 0)
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1


        return res