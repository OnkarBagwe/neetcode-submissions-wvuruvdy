class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two pointer:
        # l, r = 0, 1
        # maxPrice = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxPrice = max(maxPrice, profit)
        #     else:
        #         l = r
        #     r += 1
        # return maxPrice

        #DP:
        buy = prices[0]
        maxProfit = 0
        
        for p in prices[1:]:
            maxProfit = max(maxProfit, p - buy)
            buy = min(buy, p)
            
        return maxProfit