class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # resRow = []

        # for row in matrix:
        #     l = 0
        #     r = len(row) - 1
        #     if row[l] <= target and row[r] >= target:
        #         resRow = row

        # l = 0
        # r = len(resRow) - 1

        # while l <= r:
        #     m = l + ((r - l)//2)
        #     if resRow[m] > target:
        #         r = m - 1
        #     elif resRow[m] < target:
        #         l = m + 1 
        #     else:
        #         return True
        # return False


        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // COLS, m % COLS
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
        