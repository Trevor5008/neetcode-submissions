class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        numSums, runSum = {0: 1}, 0
        total = 0
        for r in range(len(nums)):
            runSum += nums[r]
            if runSum - k in numSums:
                total += numSums.get(runSum - k)
            numSums[runSum] = numSums.get(runSum, 0) + 1
        return total