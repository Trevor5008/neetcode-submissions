class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = {}
        length = 0
        max_len = 0
        for i in range(len(nums)):
            vals[nums[i]] = i
        
        for k, v in vals.items():
            if k - 1 not in vals:
                length = 0
                while k + length in vals:
                    length += 1
                    max_len = max(max_len, length)
        return max_len