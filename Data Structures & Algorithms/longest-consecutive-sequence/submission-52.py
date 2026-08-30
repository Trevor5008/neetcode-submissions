class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valSet = set(nums)
        longest = 0
        for val in valSet:
            if (val - 1) not in valSet:
                length = 1
                while (val + length) in valSet:
                    length += 1
                longest = max(longest, length)
        return longest 