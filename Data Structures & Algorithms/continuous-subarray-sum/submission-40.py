class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runSums, runSum = {0: -1}, 0
        for idx, num in enumerate(nums):
            runSum += num
            if runSum % k in runSums:
                if (idx - runSums[runSum % k]) >= 2:
                    return True
            else: runSums[runSum % k] = idx
        return False