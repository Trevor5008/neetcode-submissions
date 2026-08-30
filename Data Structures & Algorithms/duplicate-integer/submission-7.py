class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vals = set()
        for val in nums:
            if val in vals:
                return True
            vals.add(val)
        return False