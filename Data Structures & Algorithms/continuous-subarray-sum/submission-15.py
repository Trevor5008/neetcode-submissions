class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            remainder = currSum % k
            if remainder in remainders:
                if i - remainders[remainder] >= 2:
                    return True
            else:
                remainders[remainder] = i
        return False