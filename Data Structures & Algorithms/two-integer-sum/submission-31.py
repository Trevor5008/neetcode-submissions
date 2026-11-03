class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in sums:
                return [sums[diff], idx]
            sums[val] = idx
        return []