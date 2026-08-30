from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [((x**2 + y**2), x, y) for x, y in points]
        heapq.heapify(points)
        res = []
        while k > 0:
            k -= 1
            x, y, z = heapq.heappop(points)
            res.append([y, z])
        return res