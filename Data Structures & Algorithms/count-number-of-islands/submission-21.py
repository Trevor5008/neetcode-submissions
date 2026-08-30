from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0]) 
        visited = set()
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        q = deque()
        islands = 0

        def bfs(r, c):
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1'
                    and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc)) 

                

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands