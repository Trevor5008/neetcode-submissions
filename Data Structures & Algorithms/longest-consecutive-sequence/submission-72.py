class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length, max_len = 0, 0
        for k in num_set:
            if k - 1 not in num_set:
                length = 0
                while length + k in num_set:
                    length += 1
                    max_len = max(max_len, length)
        return max_len