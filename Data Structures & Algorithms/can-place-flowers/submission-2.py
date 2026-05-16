class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # flowerbed = [0] + flowerbed + [0]

        # for i in range(1, len(flowerbed) - 1):
        #     if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
        #         flowerbed[i] = 1
        #         n -= 1
        
        # return n<=0

        empty = 0 if flowerbed[0] else 1

        for f in flowerbed:
            if f:
                n -= int((empty - 1) / 2)
                empty = 0
            else:
                empty += 1

        n -= empty // 2
        return n <= 0