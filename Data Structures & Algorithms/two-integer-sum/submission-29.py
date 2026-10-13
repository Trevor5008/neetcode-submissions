class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in diffs: return [diffs[diff], i]
            diffs[v] = i
        return []