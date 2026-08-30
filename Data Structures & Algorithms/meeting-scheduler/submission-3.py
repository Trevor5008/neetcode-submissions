class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(slots)

        while len(slots) > 1:
            start1, end1 = heapq.heappop(slots)
            start2, end2 = slots[0]

            if end1 >= start2 + duration:
                start = max(start1, start2)
                return [start, start + duration]

        return []