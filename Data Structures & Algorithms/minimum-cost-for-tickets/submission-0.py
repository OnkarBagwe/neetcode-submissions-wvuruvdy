class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #TOP-DOWN
        cost_map = {1: costs[0],
                    7: costs[1],
                    30: costs[2]
                    }
        dp = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")
            for d,c in cost_map:
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)
        
        #BOTTOM-UP
        # cost_map = {1: costs[0],
        #             7: costs[1],
        #             30: costs[2]
        #             }
        # n = len(days)
        # dp = [0]*(n+1)

        # for i in range(n,-1,-1):
        #     j = i
        #     dp[i] = float("inf")
        #     for d,c in cost_map:
        #         j = i
        #         while j < len(days) and days[j] < days[i] + d:
        #             j += 1
        #         dp[i] = min(dp[i], c + dp[j])
        # return dp[0]