class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumsMap = {0: 1}
        total, currSum = 0, 0
        for num in nums:
            currSum += num
            if currSum - k in sumsMap:
                total += sumsMap[currSum - k]
            sumsMap[currSum] = sumsMap.get(currSum, 0) + 1
        return total
