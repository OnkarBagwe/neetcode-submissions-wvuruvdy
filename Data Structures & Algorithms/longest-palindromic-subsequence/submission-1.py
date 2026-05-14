# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         l1 = len(text1)
#         l2 = len(text2)

#         dp = [[0 for j in range(l2+1)] for i in range(l1+1)]

#         for i in range(l1-1, -1, -1):
#             for j in range(l2-1,-1,-1):
#                 if text1[i] == text2[j]:
#                     dp[i][j] = 1 + dp[i+1][j+1]
#                 else:
#                     dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
#         return dp[0][0]

#     def longestPalindromeSubseq(self, s: str) -> int:
#         return self.longestCommonSubsequence(s,s[::-1])

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        #Top Down:
        cache = {}

        def dfs(i,j):
            if i > j:
                return 0
            if i == j:
                return 1
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == s[j]:
                cache[(i,j)] = dfs(i+1, j-1) + 2
            else:
                cache[(i,j)] = max(dfs(i+1,j), dfs(i,j-1))

            return cache[(i,j)]

        return dfs(0, len(s)-1)