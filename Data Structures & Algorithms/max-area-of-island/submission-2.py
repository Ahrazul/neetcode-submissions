class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        res = []

        def bfs(coords):
            area = 1
            q = deque([coords])
            while q:
                a,b = q.popleft()
                visit.add((a,b))
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
                        area += 1
            res.append(area)

        for r in range(ROWS):
            for c in range(COLS):
                if (
                    (grid[r][c] == 1) and 
                    ((r,c) not in visit)
                ):
                    bfs((r,c))

        if not res:
            return 0
        else:
            return max(res)



        