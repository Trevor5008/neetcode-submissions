"""
Given an array of integers 'nums' and an integer 'k'
return the total number of subarrays whose sum == k

Ex1: [2,-1,1,2], k = 2 -> 4 ([2], [2,-1,1], [-1,1,2],[2])
sums = {0:1, }
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = {0:1}
        currSum, count = 0, 0
        for num in nums:
            currSum += num
            if (currSum - k) in sums:
                count += sums[currSum - k]
            sums[currSum] = sums.get(currSum, 0) + 1

        return count