class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for crs, preq in prerequisites:
            adj[crs].append(preq)

        courses = [0 for _ in range(numCourses)]

        # Cycle detection
        def dfs(course):
            courses[course] = 1 # visiting

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