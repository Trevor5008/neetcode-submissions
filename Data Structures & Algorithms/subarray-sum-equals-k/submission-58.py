class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}
        currSum, total = 0, 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum - k in prefixSums:
                total += prefixSums.get(currSum - k)
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        print(prefixSums)
        return total