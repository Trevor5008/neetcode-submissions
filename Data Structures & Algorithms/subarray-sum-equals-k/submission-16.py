class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        prefixSums = {0:1}
        # [2,-1,1,2]
        for num in nums:
            currSum += num
            if currSum - k in prefixSums:
                res += prefixSums[currSum - k]
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1 
        return res