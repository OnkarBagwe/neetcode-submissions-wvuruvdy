class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        def isPali(i,j):
            nonlocal res, resLen
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i+1) > resLen:
                    resLen = j-i+1
                    res = s[i:j+1]
                i -= 1
                j += 1
            return res

        for i in range(len(s)):
            #odd
            res = isPali(i,i)
            #even
            res = isPali(i,i+1)
        
        return res


        

        

        #DP:
        # res = ""
        # resLen = 0
        # n = len(s)

        # dp = [[False]*n for _ in range(n)]

        # for i in range(n - 1, -1, -1):
        #     for j in range(i,n):
        #         if s[i] == s[j] and (j - i <=2 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             if resLen < (j - i + 1):
        #                 res = s[i:j+1]
        #                 resLen = j - i + 1
        
        # return res