class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {} # (r,c) -> LIP

        def dfs(r, c, prevVal):
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prevVal:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]

            res = 1
            res = max(res, 1 + dfs(r+1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r-1,c,matrix[r][c]))
            res = max(res, 1 + dfs(r,c+1,matrix[r][c]))
            res = max(res, 1 + dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)

        return max(dp.values())