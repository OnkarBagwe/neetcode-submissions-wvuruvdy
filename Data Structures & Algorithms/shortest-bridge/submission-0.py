class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def invalid(r,c):
            return r not in range(N) or c not in range(N)
        
        visited = set()

        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visited):
                return
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)

        def bfs():
            res = 0
            q = deque(visited)
            while q:
                for _ in range(len(q)):
                    r,c = q.popleft()
                    for dr,dc in directions:
                        nr,nc = r+dr,c+dc
                        if invalid(nr,nc) or (nr,nc) in visited:
                            continue
                        if grid[nr][nc]:
                            return res
                        q.append((nr,nc))
                        visited.add((nr,nc))
                res += 1
            return res


        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()