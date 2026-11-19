class NumArray:

    def __init__(self, nums: List[int]):
        self.pfxSums = {-1: 0}
        for i in range(len(nums)):
            self.pfxSums[i] = self.pfxSums[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pfxSums[right] - self.pfxSums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)