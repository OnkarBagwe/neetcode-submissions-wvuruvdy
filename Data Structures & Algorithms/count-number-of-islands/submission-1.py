class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()

                for dr,dc in directions:
                    R,C = row+dr, col+dc
                    if (R in range(ROWS) and C in range(COLS) and grid[R][C] == "1" and (R,C) not in visit):
                        q.append((R,C))
                        visit.add((R,C))



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1
        return islands