class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            val1 = self.minHeap[0]
            val2 = -self.maxHeap[0]
            return (val1 + val2) / 2.0
        else:
            return -self.maxHeap[0]
        