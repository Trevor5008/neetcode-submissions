from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()
        islands = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if ((nr,nc) not in visited
                     and nr in range(rows) 
                     and nc in range(cols)
                     and grid[nr][nc] == '1'):
                        visited.add((nr,nc))
                        q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    bfs(r,c)
                    islands += 1
        return islands
        