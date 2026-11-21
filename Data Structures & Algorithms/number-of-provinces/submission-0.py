class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # n cities (n == rows == cols)
        n = len(isConnected)
        provinces = 0

        def dfs(city):
            if city >= n or isConnected[city][city] == 2: 
                return 0
            isConnected[city][city] = 2
            for edge in range(n):
                if isConnected[city][edge] == 1:
                    dfs(edge)
            return 1
        for city in range(n):
            provinces += dfs(city)
        return provinces