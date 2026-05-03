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
        maxProfit = 0
        minBuy = prices[0]

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])

        return maxProfit