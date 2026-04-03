class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        #find peak
        l = 1
        r = length - 2
        while l <= r:
            m = l + (r-l)//2
            left = mountainArr.get(m-1)
            mid = mountainArr.get(m)
            right = mountainArr.get(m+1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        
        peak = m

        #Search left portion
        l = 0
        r = peak - 1

        while l <= r:
            m = l + (r-l)//2
            val = mountainArr.get(m)
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m
        
        #Search right portion (decreasing order so opposite swap for l and r)
        l = peak
        r = length - 1

        while l <= r:
            m = l + (r-l)//2
            val = mountainArr.get(m)
            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m

        return -1