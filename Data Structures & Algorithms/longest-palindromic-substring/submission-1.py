class Solution:
    def longestPalindrome(self, s: str) -> str:
        # res = ""
        # resLen = 0

        # for i in range(len(s)):
        #     #odd
        #     l,r = i,i
        #     while l >=0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r - l + 1
        #         l -= 1
        #         r += 1
        #     #even
        #     l,r = i, i+1
        #     while l >=0 and r < len(s) and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r - l + 1
        #         l -= 1
        #         r += 1

        # return res

        #DP:
        res = ""
        resLen = 0
        n = len(s)

        dp = [[False]*n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        res = s[i:j+1]
                        resLen = j - i + 1
        
        return res