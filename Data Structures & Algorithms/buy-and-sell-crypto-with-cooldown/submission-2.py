class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Buy = i+1
        #Sell = i+2

        dp = {} #(i,buying)
        
        def dfs(i,buying):
            if i >= len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i,buying)] = max(buy, dfs(i+1,buying)) # dfs(i+1,buying) -> cooldown
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i,buying)] = max(sell, dfs(i+1, buying)) # dfs(i+1,buying) -> cooldown
            
            return dp[(i,buying)]
        
        return dfs(0,True)