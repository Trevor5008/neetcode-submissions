class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        q = deque()
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh += 1
        
        minutes = 0
        while q:
            row, col, time = q.popleft()
            minutes = max(minutes, time)

            for dr, dc in dirs:
                nr, nc = dr + row, dc + col
                if (
                    nr in range(rows) and nc in range(cols)
                    and grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, time + 1))

        return minutes if fresh == 0 else -1