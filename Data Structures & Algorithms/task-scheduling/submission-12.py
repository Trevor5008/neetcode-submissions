class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_ct = Counter(tasks)
        q = deque()
        max_heap = []
        cycles = 0
        for ct in task_ct.values():
            heapq.heappush(max_heap, -ct)
        
        while q or max_heap:
            cycles += 1
            if max_heap:
                ct = -heapq.heappop(max_heap)
                if ct - 1 > 0:
                    q.append((ct - 1, cycles + n))
            if q and q[0][1] == cycles:
                heapq.heappush(max_heap, -q.popleft()[0])
        return cycles