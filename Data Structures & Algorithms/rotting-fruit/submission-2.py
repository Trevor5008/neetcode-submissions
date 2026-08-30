class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        if fresh == 0: return 0

        mins = -1
        while q:
            mins += 1
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(rows) and nc in range(cols)
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return mins if fresh == 0 else -1