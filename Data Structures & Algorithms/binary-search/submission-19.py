class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            curr = nums[mid]
            print(curr)
            if curr < target:
                left = mid + 1
                print("go right")
            elif curr > target:
                right = mid - 1
                print("go left")
            elif curr == target:
                return mid
        return -1