class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips = set()
        res = []
        for l in range(len(nums)-2):
            idx = l + 1
            r = len(nums)-1
            while idx < r:
                total = nums[l] + nums[idx] + nums[r]
                if total == 0 and (nums[l], nums[idx], nums[r]) not in trips:
                    res.append([nums[l], nums[idx], nums[r]])
                    trips.add((nums[l], nums[idx], nums[r]))
                    idx += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    idx += 1
        return res