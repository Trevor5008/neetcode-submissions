class Solution:
    # Input: integer array 'nums'
    # Output: integer array of product of all elements of 'nums'
    # Ex. [1,2,4,6] -> [2*4*6=48, 1*4*6=24, 1*2*6=12, 1*2*4=8]
    # Time: O(n), Space: O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums)+1):
            res.append(math.prod(nums[:i-1]) * math.prod(nums[i:]))
        return res
        