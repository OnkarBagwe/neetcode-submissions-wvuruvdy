class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        resRow = []

        for row in matrix:
            l = 0
            r = len(row) - 1
            if row[l] <= target and row[r] >= target:
                resRow = row
                
        l = 0
        r = len(resRow) - 1

        while l <= r:
            m = l + ((r - l)//2)
            if resRow[m] > target:
                r = m - 1
            elif resRow[m] < target:
                l = m + 1 
            else:
                return True
        return False
