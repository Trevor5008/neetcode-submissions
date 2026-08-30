class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0]*len(temperatures)
        for k, v in enumerate(temperatures):
            while temps and temps[-1][1] < v:
                idx, t = temps.pop()
                res[idx] = k - idx
            temps.append((k, v))
        return res