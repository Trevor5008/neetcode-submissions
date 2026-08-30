class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # good subarray: length >= 2, sum of subarray multiple of k
        remainder_map = {0: -1} # {remainder: idx}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            remainder = currSum % k
            if remainder in remainder_map:
                print(remainder_map)
                # check whether the subarray meets length req't
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
        return False