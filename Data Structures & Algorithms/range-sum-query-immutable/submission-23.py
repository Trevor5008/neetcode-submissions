class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        prefixSums = [0] * (len(nums) + 1)
        for i in range(1, len(prefixSums)):
            prefixSums[i] = prefixSums[i-1] + nums[i-1]
        self.prefixSums = prefixSums

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSums[right+1] - self.prefixSums[left] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)