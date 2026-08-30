class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {v: k for k, v in enumerate(nums)}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []