class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = currSum = 0
        prefixSums = {0:1}
        # [2,-1,1,2]
        for num in nums:
            currSum += num
            # currSum += 2 = 2
            # 2 += -1 = 1
            diff = currSum - k
            # diff = 2 - 2 = 0
            # diff = 1 - 2 = -1
            res += prefixSums.get(diff, 0)
            # res += 1 = 1
            # res += 0 = 1
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
            # prefixSums[2] = 1
            # prefixSums[1] = 1
        return res