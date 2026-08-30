class NumArray:

    def __init__(self, nums: List[int]):
        sums = [0]*(len(nums)+1)
        for i in range(1, len(sums)):
            sums[i] = sums[i-1] + nums[i-1]
        self.sums = sums

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)