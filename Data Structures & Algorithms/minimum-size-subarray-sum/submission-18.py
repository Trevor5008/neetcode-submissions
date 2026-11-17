class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pfxSums = [0]*(len(nums)+1)
        for i in range(len(nums)):
            pfxSums[i+1] = pfxSums[i] + nums[i]
        n = len(nums)
        res = n + 1
        for i in range(n):
            l, r = i, n
            while l < r:
                mid = (l + r) // 2
                curSum = pfxSums[mid+1] - pfxSums[i]
                if curSum >= target: r = mid
                elif curSum < target: l = mid + 1
            if l != n: res = min(res, l - i + 1)
        return res % (n + 1)