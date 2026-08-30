class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) <= 1: return len(nums)
        nums.sort()
        longest = 0
        l, r = 0, 1
        while l < r and r < len(nums):
            curr = nums[l]
            while (nums[r] - nums[l]) != (r - l):
                l += 1
                r = l
            longest = max(longest, r - l + 1)
            r += 1
        return longest