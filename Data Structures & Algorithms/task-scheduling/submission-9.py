class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cts = Counter(tasks)
        max_heap = []
        q = deque()
        cycles = 0
        for ct in task_cts.values():
            heapq.heappush(max_heap, -ct)

        while max_heap or q:
            cycles += 1
            if max_heap:
                count = -heapq.heappop(max_heap)
                if count - 1 > 0:
                    # cycles + n represents the time when avail
                    q.append((count - 1, cycles + n))

            if q and q[0][1] == cycles:
                heapq.heappush(max_heap, -q.popleft()[0])
        return cycles