"""
Given an array of temperatures (where temps[i] represents the daily temp on
the ith day)

return an array `result` where result[i] is the number of days after the ith day
before a warmer temperature appears on a future day.
set result[i] = 0 if there is no future day where the temp is warmer

Ex1: temps = [30,38,30,36,35,40,28] -> [1,4,1,2,1,0,0]
Ex2: temps = [22,21,20] -> [0,0,0]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                results[stackInd] = i - stackInd
            stack.append((t, i))
        return results