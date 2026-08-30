class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            while len(stack) and stack[-1][1] < currTemp:
                idx, temp = stack.pop()
                res[idx] = i - idx
            stack.append((i, currTemp))
        return res