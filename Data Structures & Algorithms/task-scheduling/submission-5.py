class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        q, max_heap = deque(), []
        cycles = 0
        for ct in counts.values():
            heapq.heappush(max_heap, -ct)
        
        while max_heap or q:
            cycles += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt < 0:
                    q.append((cnt, cycles + n))
            if q and q[0][1] == cycles:
                heapq.heappush(max_heap, q.popleft()[0])
        return cycles