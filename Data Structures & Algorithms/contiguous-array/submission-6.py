class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre_sums = {0: -1}        
        longest, curr_sum = 0, 0
        for i in range(len(nums)):
            curr_sum += (1 if nums[i] == 1 else -1)
            if curr_sum in pre_sums:
                longest = max(longest, i - pre_sums[curr_sum])
            else: pre_sums[curr_sum] = i
        return longest