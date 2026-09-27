class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for i in range(numCourses)]

        for crs, preq in prerequisites:
            adjList[crs].append(preq)

        courses = [0 for i in range(numCourses)]
        # cycle detection
        def dfs(course):
            courses[course] = 1 # visiting

            for preq in adjList[course]:
                if courses[preq] == 1:
                    return True 
                elif courses[preq] == 0:
                    if dfs(preq): return True
            courses[course] = 2 # processed
            return False

        for i in range(len(courses)):
            if courses[i] == 0 and dfs(i):
                return False

        return True