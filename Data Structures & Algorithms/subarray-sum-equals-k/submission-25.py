class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumsCount = {0:1} # 0 appears once
        runSum = 0
        total = 0
        for i in range(len(nums)):
            runSum += nums[i]
            if runSum - k in sumsCount:
                total += sumsCount[runSum-k]
            sumsCount[runSum] = sumsCount.get(runSum, 0) + 1
        return total