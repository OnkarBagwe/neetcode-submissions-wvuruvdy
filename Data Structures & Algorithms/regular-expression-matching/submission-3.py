class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # #TOP-DOWN
        # cache = {}
        # def dfs(i,j):
        #     if (i,j) in cache:
        #         return cache[(i,j)]
        #     if i >=len(s) and j >=len(p):
        #         return True
        #     if j >= len(p):
        #         return False

        #     match = i<len(s) and (s[i]==p[j] or p[j] == ".")

        #     if (j+1) < len(p) and p[j+1] == "*":
        #         cache[(i,j)] = (dfs(i, j+2) or (match and dfs(i+1,j)))
        #         return cache[(i,j)]
            
        #     if match:
        #         cache[(i,j)] = dfs(i+1,j+1)
        #         return cache[(i,j)]
        #     cache[(i,j)] = False
        #     return cache[(i,j)]
        
        # return dfs(0,0)
        

        #BOTTOM-UP:
        m = len(s)
        n = len(p)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[m][n] = True

        for i in range(m,-1,-1):
            for j in range(n-1,-1,-1):
                match = i < m and (s[i] == p[j] or p[j] == ".")

                if (j+1) < n and p[j+1] == "*":
                    dp[i][j] = dp[i][j+2]
                    if match:
                        dp[i][j] = dp[i+1][j] or dp[i][j]
                elif match:
                    dp[i][j] = dp[i+1][j+1]
        
        return dp[0][0]