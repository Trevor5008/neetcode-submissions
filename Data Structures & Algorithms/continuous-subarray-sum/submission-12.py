class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1} # {remainder: idx}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            remainder = currSum % k
            if remainder in remainder_map and i - remainder_map[remainder] >= 2:
                return True
            elif remainder not in remainder_map:
                remainder_map[remainder] = i
        return False