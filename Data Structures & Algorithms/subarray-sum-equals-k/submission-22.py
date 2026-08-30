class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        currSum = 0
        total = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum - k in counts:
                total += counts[currSum - k]
            counts[currSum] = counts.get(currSum, 0) + 1
        return total