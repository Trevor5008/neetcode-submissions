"""
Given an array of length 'n', which was originally in sorted ascending order,
it has now been rotated b/n 1 and n times

Return the minimum element of this array
Ex1: [3,4,5,6,1,2] -> 1
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        res = nums[0]
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            mid = (r + l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res