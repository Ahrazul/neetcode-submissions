class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            a,b = q.popleft()
            for dx,dy in dirs:
                x, y = a + dx, b + dy
                if (
                    (0 <= x < ROWS) and 
                    (0 <= y < COLS) and
                    (grid[x][y] == INF)
                ):
                    grid[x][y] = grid[a][b] + 1
                    q.append((x,y))
        