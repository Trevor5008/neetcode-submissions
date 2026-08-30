class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        runSum = 0
        count = 0
        for num in nums:
            runSum += num
            print(runSum)
            if (runSum - k) in prefixSums:
                count += prefixSums[runSum - k]
            prefixSums[runSum] = prefixSums.get(runSum, 0) + 1
        return count
            