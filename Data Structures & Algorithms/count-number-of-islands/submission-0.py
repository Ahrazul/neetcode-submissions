class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        res = 0
        visited = set()
        dirs = [[0,1], [1,0], [-1,0], [0,-1]]
        
        def bfs(i,j):
            q = deque([(i,j)])
            visited.add((i,j))
            while q:
                a,b = q.popleft()
                for dx,dy in dirs:
                    x = a + dx
                    y = b + dy

                    if (0 <= x < r and 0 <= y < c and grid[x][y] == '1' and (x,y) not in visited):
                        q.append((x,y))
                        visited.add((x,y))

            
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    res += 1

        return res




