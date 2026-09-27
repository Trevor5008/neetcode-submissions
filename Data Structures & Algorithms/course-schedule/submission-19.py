class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        for crs, preq in prerequisites:
            adj[crs].append(preq)

        courses = [0 for _ in range(numCourses)]

        def dfs(course):
            courses[course] = 1 # visiting

            for preq in adj[course]:
                if courses[preq] == 1:
                    return True
                elif courses[preq] == 0:
                    if dfs(preq):
                        return True
            courses[course] = 2
            return False

        for i in range(len(courses)):
            if courses[i] == 0 and dfs(i):
                return False

        return True