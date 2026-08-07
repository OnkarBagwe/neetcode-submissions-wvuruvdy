class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days

        while l <= r:
            cap = l + ((r-l)//2) 
            d = 0
            if canShip(cap):
                res= min(res,cap)
                r = cap-1
            else:
                l = cap+1
        
        return res