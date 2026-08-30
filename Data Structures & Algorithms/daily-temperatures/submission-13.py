class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            currTemp = temperatures[i]
            print(f"at index {i}, stack = {stack}")
            while stack and stack[-1][1] < currTemp:
                last = stack.pop()
                res[last[0]] = i - last[0]
            stack.append((i, currTemp))
        return res