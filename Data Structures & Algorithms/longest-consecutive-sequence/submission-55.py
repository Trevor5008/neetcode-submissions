class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 not in numSet:
                currLen = 1
                curr = num
                while curr + 1 in numSet:
                    currLen += 1
                    curr += 1
                longest = max(longest, currLen)
        return longest