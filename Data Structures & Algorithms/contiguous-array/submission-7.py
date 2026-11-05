class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sums = {0: -1}
        longest = 0

        runSum = 0
        for i in range(len(nums)):
            runSum += (1 if nums[i] == 1 else -1)
            if runSum in sums:
                longest = max(longest, i - sums[runSum])
            else: sums[runSum] = i 
        return longest