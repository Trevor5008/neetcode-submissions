class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = { 0: 1}
        count = 0
        currSum = 0
        for key, v in enumerate(nums):
            currSum += v
            if currSum - k in sums:
                count += sums.get(currSum - k)
            sums[currSum] = sums.get(currSum, 0) + 1
        return count