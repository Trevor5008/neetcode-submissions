class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            curr = nums[mid]
            if curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                return mid
        return -1