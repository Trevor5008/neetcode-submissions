class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixSums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prefixSums[i+1] = self.prefixSums[i] + nums[i]


    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSums[right + 1] - self.prefixSums[left]