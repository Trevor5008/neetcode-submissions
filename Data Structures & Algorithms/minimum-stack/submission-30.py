class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if self.minStack and self.minStack[-1] >= val or not self.minStack:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        el = self.stack.pop()
        if self.minStack and self.minStack[-1] == el:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]