class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runSum, modMap = 0, {0: -1}
        for key, v in enumerate(nums):
            runSum += v
            if runSum % k in modMap:
                if key - modMap[runSum % k] >= 2:
                    return True
            else:
                modMap[runSum % k] = key
        return False