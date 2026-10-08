class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        total, curr_sum = 0, 0
        for num in nums:
            curr_sum += num
            total += prefix_sums.get(curr_sum - k, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        return total