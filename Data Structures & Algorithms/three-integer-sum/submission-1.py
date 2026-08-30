class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            if val > 0:
                break
            if i > 0 and val == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                curr_sum = val + nums[l] + nums[r]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    print(f"[{i}:{val}, {l}:{nums[l]}, {r}:{nums[r]}]")
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res