class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {0: 1}
        total = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num 
            total += prefix_sums.get(curr_sum - k, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        print(prefix_sums)
        return total