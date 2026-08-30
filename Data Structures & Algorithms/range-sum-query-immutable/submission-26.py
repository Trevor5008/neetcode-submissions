class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        sumMap = {0:0}
        for i in range(len(nums)):
            sumMap[i+1] = sumMap[i] + nums[i]
        self.sumMap = sumMap

    def sumRange(self, left: int, right: int) -> int:
        return self.sumMap[right+1] - self.sumMap[left]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)