class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {v: k for k, v in enumerate(nums)}
        for k, v in enumerate(nums):
            diff = target - v
            if diff in indices and indices[diff] > k:
                return [k, indices[diff]]
        return []