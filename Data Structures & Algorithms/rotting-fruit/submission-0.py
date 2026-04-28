class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    a, b = x + dx, y + dy

                    if (
                        a < 0 or a == rows or 
                        b < 0 or b == cols or 
                        grid[a][b] != 1
                    ):
                        continue
                    grid[a][b] = 2
                    fresh -= 1
                    q.append((a,b))
            time += 1

        return time if fresh == 0 else -1