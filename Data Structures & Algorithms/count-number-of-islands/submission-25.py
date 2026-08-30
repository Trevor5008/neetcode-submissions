class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        q = collections.deque()
        visited = set()
        islands = 0

        def bfs(r, c):
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr in range(rows) and nc in range(cols)
                    and (nr, nc) not in visited and grid[nr][nc] == '1'):
                        visited.add((nr, nc))
                        q.append((nr, nc)) 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        return islands