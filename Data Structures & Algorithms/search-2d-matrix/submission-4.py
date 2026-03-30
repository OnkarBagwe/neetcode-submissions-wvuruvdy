class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        resRow = []

        for row in matrix:
            l = 0
            r = len(row) - 1
            if row[l] <= target and row[r] >= target:
                resRow = row

        print(resRow)
        l = 0
        r = len(resRow) - 1

        while l <= r:
            m = l + ((r - l)//2)
            if resRow[m] > target:
                r = m - 1
                print(r)
            elif resRow[m] < target:
                l = m + 1 
                print(l)
            else:
                print(resRow[m])
                return True
        return False
