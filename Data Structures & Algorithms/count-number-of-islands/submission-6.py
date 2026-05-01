class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        res = 0
        visited = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visited and grid[nr][nc] == "1":
                        q.append((nr,nc))
                        visited.add((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    res += 1

        return res

        if not grid:
            return 0