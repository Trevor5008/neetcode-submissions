"""
Design a stack class that supports push, pop, top and getMin ops
"""
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minVal = self.stack[0]
        for val in self.stack:
            if val < minVal:
                minVal = val
        return minVal
