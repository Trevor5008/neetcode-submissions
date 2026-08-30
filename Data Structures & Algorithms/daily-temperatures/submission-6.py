class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            val = temperatures[i]
            r = i + 1
            while r < len(temperatures) and temperatures[r] <= val:
                r += 1
            if r < len(temperatures) and temperatures[r] > val:
                res.append(r - i)
            else:
                res.append(0)
        return res
                