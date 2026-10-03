class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = [[] for _ in range(numCourses)]
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
        courses = [0 for _ in range(numCourses)]        

        def dfs(course):
            courses[course] = 1 # visiting

            for preq in preqs[course]:
                if courses[preq] == 1:
                    return True
                elif courses[preq] == 0:
                    if dfs(preq):
                        return True
            courses[course] = 2
        for i in range(len(courses)):
            if courses[i] == 0 and dfs(i):
                return False
        return True