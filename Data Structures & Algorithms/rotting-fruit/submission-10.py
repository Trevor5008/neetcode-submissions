class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        mins = 0
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col, mins))

        while q:
            row, col, mins = q.popleft()

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if (
                    nr in range(rows) and
                    nc in range(cols) and 
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, mins + 1))
        return mins if fresh <= 0 else -1