class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        currSum = 0
        count = 0
        for num in nums:
            currSum += num
            if currSum - k in prefixSums:
                count += prefixSums.get(currSum - k)
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        return count