class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumsCnt = {0:1}
        numSubs, runSum = 0, 0
        for i in range(len(nums)):
            runSum += nums[i]
            if runSum - k in sumsCnt:
                numSubs += sumsCnt[runSum - k]
            sumsCnt[runSum] = sumsCnt.get(runSum, 0) + 1
        return numSubs