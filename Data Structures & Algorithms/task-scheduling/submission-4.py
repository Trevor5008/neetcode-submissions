class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q, max_heap, task_ct = deque(), [], Counter(tasks)
        for ct in task_ct.values():
            heapq.heappush(max_heap, -ct)
        
        cycles = 0
        while max_heap or q:
            cycles += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt < 0:
                    q.append((cnt, cycles + n))
            if q and q[0][1] == cycles:
                heapq.heappush(max_heap, q.popleft()[0])
        return cycles