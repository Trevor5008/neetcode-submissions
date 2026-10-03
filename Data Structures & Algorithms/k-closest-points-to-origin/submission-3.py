from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for coords in points:
            dist = -sqrt(coords[0]**2 + coords[1]**2)
            heapq.heappush(heap, (dist, coords))
            while len(heap) > k:
                heapq.heappop(heap)
        return [coords for dist, coords in heap]