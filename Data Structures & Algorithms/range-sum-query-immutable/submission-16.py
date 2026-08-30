from collections import Counter

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        prefixSums = {}
        currSum = 0
        for i in range(len(self.nums)):
            currSum += self.nums[i]
            prefixSums[i] = currSum
        self.prefixSums = prefixSums

    def sumRange(self, left: int, right: int) -> int:
        #          0   1   2   3   4   5
        # nums = [-2,  0,  3, -5,  2, -1]
        # sums = [-2, -2,  1, -4, -2, -3]
        # left = 2, right = 5 -> -1 ()
        # 
        leftSum = self.prefixSums[left - 1] if left > 0 else 0
        return self.prefixSums[right] - leftSum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)