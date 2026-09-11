class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while temps and temps[-1][1] < temp:
                idx, t = temps.pop()
                res[idx] = i - idx
            temps.append((i, temp))
        return res