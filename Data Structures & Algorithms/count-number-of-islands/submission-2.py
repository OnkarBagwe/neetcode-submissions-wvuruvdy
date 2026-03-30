class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr,dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visit.add((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands