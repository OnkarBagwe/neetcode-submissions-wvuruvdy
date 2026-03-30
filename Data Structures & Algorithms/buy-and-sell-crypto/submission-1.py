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
        minPrice = prices[0]
        maxPrice = 0

        for s in prices:
            maxPrice = max(maxPrice, s - minPrice)
            minPrice = min(minPrice, s)
        return maxPrice