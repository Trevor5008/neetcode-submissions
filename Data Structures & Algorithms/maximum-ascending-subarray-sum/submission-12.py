class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, 1
        currSum = nums[l]
        maxSum = currSum
        while l < r and r < len(nums):
            curr, nxt = nums[r-1], nums[r]
            if curr < nxt:
                currSum += nxt
                r += 1
                maxSum = max(currSum, maxSum)
            else:
                l = r
                currSum = nums[l]
                r += 1
        return maxSum