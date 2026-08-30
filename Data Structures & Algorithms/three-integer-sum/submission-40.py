class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        trips = set()
        for l in range(len(nums)-2):
            r = len(nums)-1
            idx = l + 1
            while idx < r:
                total = nums[l] + nums[idx] + nums[r]
                if total == 0 and (nums[l], nums[idx], nums[r]) not in trips:
                    trips.add((nums[l], nums[idx], nums[r]))
                    res.append([nums[l], nums[idx], nums[r]])
                    r -= 1
                    idx += 1
                elif total > 0:
                    r -= 1
                else:
                    idx += 1
        return res
