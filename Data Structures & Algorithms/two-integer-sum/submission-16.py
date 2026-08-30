class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valMap = {v: k for k, v in enumerate(nums)}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in valMap and valMap[diff] != i:
                return [i, valMap[diff]]
        return [] 