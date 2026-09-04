class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0]*len(temperatures)
        stackTemps = []
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            while stackTemps and stackTemps[-1][0] < currTemp:
                temp, idx = stackTemps.pop()
                temps[idx] = i - idx
            stackTemps.append((currTemp, i))
        return temps