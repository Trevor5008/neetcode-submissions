class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum, numSubs = 0, 0

        counts = {0:1}
        for num in nums:
            currSum += num

            if currSum - k in counts:
                numSubs += counts[currSum - k]
            
            counts[currSum] = counts.get(currSum, 0) + 1
        return numSubs