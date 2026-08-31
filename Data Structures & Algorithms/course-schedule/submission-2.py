class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)} 
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = [0] * numCourses

        def hasCycle(v):
            if visited[v] == 1: return True
            elif visited[v] == 2: return False
            visited[v] = 1
            for neighbor in adj[v]:
                if hasCycle(neighbor): return True
            visited[v] = 2
            return False

        for i in range(numCourses):
            if hasCycle(i): return False
        return True
