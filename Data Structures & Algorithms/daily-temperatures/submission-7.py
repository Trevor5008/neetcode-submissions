"""
Given an array of temperatures as integers, where temperatures[i]
represents the daily temperature on the ith day.

return an array result where result[i] is the number of days after
the ith day before a warmer temperature appears on a future day

* if no future day, set result[i] to 0

Ex1: [30,38,36,35,40,28] -> [1,4,1,2,1,0,0]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures)
        for i in range(len(res)):
            curr = temperatures[i]
            for r in range(i + 1, len(temperatures)):
                if curr < temperatures[r]:
                    res[i] = r - i
                    break

        return res