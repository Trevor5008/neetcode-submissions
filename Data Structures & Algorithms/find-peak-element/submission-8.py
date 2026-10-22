class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        max_val = (float("-inf"), -1)
        while l <= r:
            mid = (l + r) // 2
            if mid + 1 <= r and nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
            max_val = max(max_val, (nums[mid], mid))
        return max_val[1]