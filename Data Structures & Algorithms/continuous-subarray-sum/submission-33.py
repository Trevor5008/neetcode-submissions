class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runSum = 0
        sums = {0: -1}
        for r in range(len(nums)):
            runSum += nums[r]
            if runSum % k in sums:
                if r - sums[runSum % k] >= 2:
                    return True
            else:
                sums[runSum % k] = r
        return False
