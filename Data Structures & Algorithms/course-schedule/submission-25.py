class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = [[] for _ in range(numCourses)]
        for crs, preq in prerequisites:
            preqs[crs].append(preq)
    
        courses = [0 for _ in range(numCourses)]
        def dfs(course):
            courses[course] = 1 # visiting

            for pre in preqs[course]:
                if courses[pre] == 0:
                    if dfs(pre): return True
                elif courses[pre] == 1:
                     return True
            courses[course] = 2 # processed
            
        for i in range(len(courses)):
            print(courses[i])
            if courses[i] == 0 and dfs(i):
                return False
        return True