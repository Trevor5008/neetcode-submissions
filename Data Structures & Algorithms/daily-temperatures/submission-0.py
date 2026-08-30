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
        results = []

        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            j = i + 1
            while j < len(temperatures):
                nextTemp = temperatures[j]
                if nextTemp > currTemp:
                    results.append(j - i)
                    break
                j += 1
            if len(results) < (i + 1):
                results.append(0)

        return results