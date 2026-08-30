class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumMap = {0:0}
        for i in range(1, len(nums) + 1):
            sumMap[i] = nums[i-1] + sumMap[i-1]
        print(sumMap)
        total = sumMap[len(nums)]
        for i in range(1, len(sumMap.keys())):
            if total - sumMap[i] == sumMap[i-1]:
                return i-1
        return -1