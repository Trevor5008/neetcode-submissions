class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0]*len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i, t = stack.pop()
                temps[i] = idx - i
            stack.append((idx, temp))
        return temps