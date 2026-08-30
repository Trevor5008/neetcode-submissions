class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = [0]*len(nums)
        prefixSums[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSums[i] = nums[i] + prefixSums[i-1]
        total = prefixSums[-1]
        if total - prefixSums[0] == 0: return 0
        for j in range(len(prefixSums)):
            if total - prefixSums[j] == prefixSums[j-1]:
                return j
        return -1