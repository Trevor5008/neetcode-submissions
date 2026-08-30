class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        prefixSums = {0:1}
        # [2,-1,1,2]
        for num in nums:
            currSum += num
            res += prefixSums.get(currSum - k, 0)
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1 
        return res