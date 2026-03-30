class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visit = set()
        res = 0

        def bfs(r,c):
            q = deque()
            q.append((r,c))

            visit.add((r,c))

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+row,dc+col
                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visit.add((nr,nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    bfs(r,c)
                    res += 1
        
        return res

        if not grid:
            return 0