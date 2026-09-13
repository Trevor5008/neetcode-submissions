class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        courses = [0 for i in range(numCourses)]

        def dfs(course): # cycle detection
            courses[course] = 1 # visited

            for pre in adj[course]:
                if courses[pre] == 1:
                    return True
                elif courses[pre] == 0:
                    if dfs(pre):
                        return True
            courses[course] = 2 # processed
            return False

        for i in range(len(courses)):
            if courses[i] == 0 and dfs(i):
                return False

        return True 