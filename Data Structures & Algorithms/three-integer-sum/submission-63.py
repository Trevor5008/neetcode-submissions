class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1
            while l < r:
                diff = nums[i] + nums[l] + nums[r]
                if diff == 0 and (nums[i], nums[l], nums[r]) not in res:
                    res.append((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif diff < 0: l += 1
                else: r -= 1
        return [[a, b, c] for a, b, c in res]