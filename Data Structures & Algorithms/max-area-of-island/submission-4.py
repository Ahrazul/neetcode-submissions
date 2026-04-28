class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        best = 0

        def bfs(start):
            area = 0
            q = deque([start])
            visit.add((start))

            while q:
                a,b = q.popleft()
                area += 1
                for dx,dy in dirs:
                    x, y = a + dx, b + dy
                    if (
                        (0 <= x < ROWS) and 
                        (0 <= y < COLS) and
                        ((x,y) not in visit) and 
                        (grid[x][y] == 1)
                    ):
                        q.append((x,y))
                        visit.add((x,y))
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (
                    (grid[r][c] == 1) and 
                    ((r,c) not in visit)
                ):
                    best = max(best, bfs((r,c)))

        return best



        