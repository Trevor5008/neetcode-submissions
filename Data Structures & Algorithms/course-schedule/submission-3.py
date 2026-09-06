class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        classes = {i: 0 for i in range(numCourses)}
        # cycle detection
        def dfs(course):
            classes[course] = 1 # mark as visited

            for pre in adj[course]:
                if classes[pre] == 1:
                    return True # cycle detected
                elif classes[pre] == 0:
                    if dfs(pre):
                        return True
            classes[course] = 2 # processed / taken
            return False

        for course in range(numCourses):
            if classes[course] == 0:
                if dfs(course): # True = cycle detected
                    return False
        
        return True