class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i + 1, len(nums)-1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l+1] and l + 1 < r:
                        l += 1
                    while nums[r] == nums[r-1] and r - 1 > l:
                        r -= 1
                    l += 1
                    r -= 1
        return res
                    