class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        vals = set(nums)
        longest = 0
        for val in vals:
            if (val - 1) not in vals:
                current_num = val
                count = 1
                while (current_num + 1) in vals:
                    current_num += 1
                    count += 1
                longest = max(longest, count)
        return longest