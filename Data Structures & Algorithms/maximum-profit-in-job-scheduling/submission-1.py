class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #TOP-DOWN:
        # n = len(startTime)
        # intervals = sorted(zip(startTime, endTime, profit))

        # dp = [-1]*n

        # def dfs(i):
        #     if i == n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     #not include
        #     dp[i] = dfs(i+1)

        #     #include
        #     l = i+1
        #     r = n
        #     j = n

        #     while l < r:
        #         m = l + (r-l)//2
        #         if intervals[i][1] <= intervals[m][0]:
        #             j = m
        #             r = m
        #         else:
        #             l = m + 1
            
        #     dp[i] = max(dp[i], intervals[i][2] + dfs(j))
        #     return dp[i]

        # return dfs(0)

        #BOTTOM-UP:
        n = len(startTime)
        intervals = sorted(zip(startTime, endTime, profit))

        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            l = i+1
            r = n
            j = n

            while l < r:
                m = l + (r-l)//2
                if intervals[i][1] <= intervals[m][0]:
                    j = m
                    r = m
                else:
                    l = m + 1
            
            dp[i] = max(dp[i+1], intervals[i][2] + dp[j])

        return dp[0]