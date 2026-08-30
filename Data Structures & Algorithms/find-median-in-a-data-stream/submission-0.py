class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None: 
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
            
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        elif len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
         

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            minVal = self.minHeap[0]
            maxVal = -self.maxHeap[0]
            return (minVal + maxVal) / 2.0
        else:
            return float(-self.maxHeap[0])