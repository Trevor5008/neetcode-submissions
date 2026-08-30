class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {nums[0]: 0}
        for i in range(1, len(nums)):
            diff = target - nums[i]
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap[nums[i]] = i
        return []
