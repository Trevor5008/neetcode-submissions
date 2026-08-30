class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {0: 1}
        currSum = 0
        numSubs = 0
        for num in nums:
            currSum += num
            if currSum - k in sumMap:
                numSubs += sumMap[currSum - k]
            sumMap[currSum] = sumMap.get(currSum, 0) + 1
        print(sumMap)
        return numSubs