"""
given an integer array 'nums' of length 'n'
create an array 'ans' of length 2n where ans[i] == nums[i]
and ans[i + n] == nums[i]
"""
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:] + nums[:]
        return ans