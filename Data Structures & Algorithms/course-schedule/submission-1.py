class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisites[i] = [a,b] means b is a preq for a
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        visited = [0] * numCourses # 0: unvisited, 1: visiting, 2: visited
        print(visited)
        def hasCycle(v):
            if visited[v] == 1: return True
            if visited[v] == 2: return False
            visited[v] = 1
            for neighbor in adj[v]:
                if hasCycle(neighbor): return True
            visited[v] = 2
            return False
            
        for i in range(numCourses):
            if hasCycle(i): return False
        return True