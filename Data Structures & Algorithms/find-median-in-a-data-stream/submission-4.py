class MedianFinder:

    def __init__(self):
        self.minStack = []
        self.maxStack = []

    def addNum(self, num: int) -> None:
        if not self.maxStack or num <= -self.maxStack[0]:
            heapq.heappush(self.maxStack, -num)
        else:
            heapq.heappush(self.minStack, num)

        if len(self.maxStack) > len(self.minStack) + 1:
            val = -heapq.heappop(self.maxStack)
            heapq.heappush(self.minStack, val)
        elif len(self.minStack) > len(self.maxStack):
            val = heapq.heappop(self.minStack)
            heapq.heappush(self.maxStack, -val)

    def findMedian(self) -> float:
        if len(self.minStack) == len(self.maxStack):
            val1 = self.minStack[0]
            val2 = -self.maxStack[0]
            return (val1 + val2) / 2.0
        else:
            return -self.maxStack[0]
        