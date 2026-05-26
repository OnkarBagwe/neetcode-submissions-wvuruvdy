class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        intervals = sorted(zip(startTime, endTime, profit))

        dp = [-1]*n

        def dfs(i):
            if i == n:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            #not include
            dp[i] = dfs(i+1)

            #include
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
            
            dp[i] = max(dp[i], intervals[i][2] + dfs(j))
            return dp[i]

        return dfs(0)