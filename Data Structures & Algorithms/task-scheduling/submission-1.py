class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCt = Counter(tasks)
        taskHeap = []
        q = deque()
        time = 0
        for ct in taskCt.values():
            heapq.heappush(taskHeap, -ct)

        while taskHeap or q:
            time += 1
            if taskHeap:
                cnt = 1 + heapq.heappop(taskHeap)
                if cnt < 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                heapq.heappush(taskHeap, q.popleft()[0])
        
        return time