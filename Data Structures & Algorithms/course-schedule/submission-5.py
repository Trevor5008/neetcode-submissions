class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        courses = {i: 0 for i in range(numCourses)}
        def dfs(course):
            courses[course] = 1 # visited

            for pre in adj[course]:
                if courses[pre] == 1:
                    return True
                elif courses[pre] == 0:
                    if dfs(pre):
                        return True
            courses[course] = 2 # processed
            return False

        for course in range(numCourses):
            if courses[course] == 0 and dfs(course):
                return False
        return True
