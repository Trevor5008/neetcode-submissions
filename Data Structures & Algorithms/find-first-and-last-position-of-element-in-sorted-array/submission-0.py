class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                orig_mid = mid
                l, r = 0, orig_mid
                ptr1 = -1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] == target:
                        ptr1 = mid
                        r = mid - 1
                    elif nums[mid] < target:
                        l = mid + 1
                    else: r = mid - 1
                l, r = orig_mid, len(nums)-1
                ptr2 = -1
                while l <= r:
                    mid = (l + r) // 2
                    if nums[mid] == target:
                        ptr2 = mid
                        l = mid + 1
                    elif nums[mid] > target:
                        r = mid - 1
                    else: l = mid + 1
                return [ptr1, ptr2]
            elif nums[mid] < target:
                l = mid + 1
            else: r = mid - 1
        return [-1,-1]