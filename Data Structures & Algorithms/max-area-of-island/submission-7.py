class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        res = 0
        dirs = [(0,1), (0,-1), (-1,0), (1,0)]

        def bfs(i,j):
            area = 1
            q = deque([(i,j)])
            grid[i][j] = 0
            while q:
                a,b = q.popleft()
                for dx,dy in dirs:
                    x = a + dx
                    y = b + dy
                    if (
                        0 <= x < r and
                        0 <= y < c and
                        grid[x][y] == 1
                    ):
                        grid[x][y] = 0
                        q.append((x,y))
                        area += 1
            return area

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    res = max(res, bfs(i,j))

        return res



        