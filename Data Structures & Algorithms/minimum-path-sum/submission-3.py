class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])

        dp = [[float("inf")]*(N+1) for _ in range(M+1)]

        dp[M-1][N] = 0

        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

        return dp[0][0]

        #space optimized:
        # ROWS = len(grid)
        # COLS = len(grid[0])

        
        # res = [float("inf")]*(COLS+1)
        # res[COLS-1] = 0

        # for r in range(ROWS-1,-1,-1):
        #     for c in range(COLS-1,-1,-1):
        #         res[c] = grid[r][c] + min(res[c], res[c+1])
        # return res[0]