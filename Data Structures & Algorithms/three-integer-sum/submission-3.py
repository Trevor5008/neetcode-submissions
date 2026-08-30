class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for l in range(len(nums)-2):
            i, r = l + 1, len(nums)-1
            while i < r:
                total = nums[l] + nums[i] + nums[r]
                if total < 0:
                    i += 1
                elif total > 0:
                    r -= 1
                else:
                    res.add((nums[l], nums[i], nums[r]))
                    i += 1
                    r -= 1
        return [list(x) for x in res]