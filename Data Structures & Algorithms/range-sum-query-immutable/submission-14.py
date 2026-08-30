"""
Given an integer array 'nums':
1. Calculate the sum of the elements of nums b/n indices left and right inclusive (left <= right)

Ex1: Input: ["NumArray","sumRange","sumRange","sumRange"]
[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

Output: [null,1,-1,-3]
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSums = []
        curr = 0
        for num in nums:
            curr += num
            self.prefixSums.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSums[right]
        leftSum = self.prefixSums[left-1] if left > 0 else 0
        return rightSum - leftSum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)