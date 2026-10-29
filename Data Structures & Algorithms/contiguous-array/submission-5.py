class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sums = {0: -1}
        curr_sum = 0
        longest = 0
        for i in range(len(nums)):
            curr_sum += (1 if nums[i] == 1 else -1)
            if curr_sum in prefix_sums:
                longest = max(longest, i - prefix_sums[curr_sum])
            else:
                prefix_sums[curr_sum] = i
        return longest