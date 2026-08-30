class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in count_map:
                return [count_map[diff], i]
            count_map[nums[i]] = i
        return False