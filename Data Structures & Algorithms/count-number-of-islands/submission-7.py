class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        M = len(grid)
        N = len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        visited = set()
        res = 0
        
        def dfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            
            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    nr,nc = row+dr,col+dc
                    if nr in range(M) and nc in range(N) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        
        
        for r in range(M):
            for c in range(N):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        
        return res