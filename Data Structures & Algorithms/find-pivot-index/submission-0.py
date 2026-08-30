"""
Given an array of integers, calculate the index of the input array
Pivot index = index where the sum of all the numbers to the left of the index
are equal to the sum of all the numbers strictly to the right of that index

Ex1: nums = [1,7,3,6,5,6] -> 3 (sum(nums[:3]) = 11, sum(nums[4:]) = 11)
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])
            if leftSum == rightSum:
                return i
        return -1