class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        res = 0
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        
        def bfs(i,j):
            q = deque([(i,j)])
            grid[i][j] = '0'
            while q:
                a,b = q.popleft()
                for dx,dy in dirs:
                    x = a + dx
                    y = b + dy

                    if (0 <= x < r and 0 <= y < c and grid[x][y] == '1'):
                        grid[x][y] = '0'
                        q.append((x,y))

            
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i,j)

        return res