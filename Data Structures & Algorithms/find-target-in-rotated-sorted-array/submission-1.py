class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        # [3,4,5,6,1,2], target = 1
        while left <= right:
            mid = (left + right) // 2 # mid = 2
            if nums[mid] == target:
                return mid
            
            # Identify which half is sorted
            # Non-rotated sequence (normal)
            if nums[left] <= nums[mid]: # 3 <= 5
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Rotated (left > right side)
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1