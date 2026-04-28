class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        for r in range(ROWS):
            for c in [0,COLS-1]:
                if board[r][c] == "O":
                    board[r][c] = "T"
                    q.append((r,c))

        for c in range(COLS):
            for r in [0,ROWS-1]:
                if board[r][c] == "O":
                    board[r][c] = "T"
                    q.append((r,c))

        while q:
            a,b = q.popleft()
            for dx,dy in dirs:
                x, y = a + dx, b + dy

                if (
                    (0 <= x < ROWS) and 
                    (0 <= y < COLS) and
                    (board[x][y] == "O")
                ):
                    board[x][y] = "T"
                    q.append((x,y))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        