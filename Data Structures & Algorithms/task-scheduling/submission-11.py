class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCt = Counter(tasks)
        heap = []
        for val in taskCt.values():
            heapq.heappush(heap, -val)
        q = deque()
        cycles = 0
        while q or heap:
            cycles += 1
            if len(heap) > 0:
                ct = -heapq.heappop(heap)
                if ct - 1 > 0:
                    q.append((ct - 1, cycles + n))
            if q and q[0][1] == cycles:
                ct, time = q.popleft()
                heapq.heappush(heap, -ct)
        return cycles