class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n cities (n == rows == cols)
        n = len(isConnected)
        provinces = 0

        def dfs(city):
            isConnected[city][city] = 2 # mark visited
            for nei in range(n):
                if nei == city: continue
                elif (
                    isConnected[city][nei] == 1
                    and isConnected[nei][nei] == 1
                ): dfs(nei)

        for city in range(n):
            if isConnected[city][city] == 1: # unvisited
                dfs(city)
                provinces += 1
        return provinces