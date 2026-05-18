class Solution:
    def __init__(self):
        self.res = ""
        self.resLen = 0
    
    def isPali(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > self.resLen:
                self.resLen = r-l+1
                self.res = s[l:r+1]
            l -= 1
            r += 1
        return self.res

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            #odd
            self.res = self.isPali(s,i,i)
            #even
            self.res = self.isPali(s,i,i+1)
        return self.res


        

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