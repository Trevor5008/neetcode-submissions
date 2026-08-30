class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]

        l, r = 0, 1
        currSum = nums[l]
        while l <= r and r < len(nums):
            curr, nxt = nums[r-1], nums[r]
            if nxt > curr:
                currSum += nxt
                maxSum = max(currSum, maxSum)
                print(f"Max sum b/n {l}, {r} = {maxSum}")
                r += 1
            else:
                print(f"Moving left pointer to {r}")
                print(f"Moving right pointer to {r + 1}")
                l = r
                r += 1
                currSum = nums[l]
        return maxSum