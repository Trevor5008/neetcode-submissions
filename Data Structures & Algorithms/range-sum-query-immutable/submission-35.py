class NumArray:

    def __init__(self, nums: List[int]):
        runSums = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(runSums)):
            runSums[i] = nums[i-1] + runSums[i-1]
        self.runSums = runSums 
        print(self.runSums)

    def sumRange(self, left: int, right: int) -> int:
        return self.runSums[right+1] - self.runSums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)