"""
Given an integer array 'nums'
- Calculate the sum of the elements of 'nums' b/n left and right indices (inclusive)
where left <= right
- Implement the NumArray class:
    - NumArray(int[] nums) initializes the object with the int array 'nums'
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums     

    def sumRange(self, left: int, right: int) -> int:
        runSum = 0
        for i in range(left, right+1):
            runSum += self.nums[i]
        return runSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)