class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid_idx = (start + end) // 2
            mid = nums[mid_idx]
            if target < mid:
                end = mid_idx - 1
            elif target > mid:
                start = mid_idx + 1
            else: 
                return mid_idx
        return -1