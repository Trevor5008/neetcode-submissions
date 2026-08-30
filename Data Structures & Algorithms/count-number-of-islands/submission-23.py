from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]

        q = deque()
        visited = set()
        islands = 0

        def bfs(r, c):
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr + row, dc + col
                    if (nr in range(rows) and nc in range(cols)
                    and grid[nr][nc] == '1' and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1
                         
        return islands