class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = {0: -1}
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum % k in sums: 
                if i - sums[currSum % k] >= 2:
                    return True
            else:
                sums[currSum % k] = i
        print(sums)
        return False
                