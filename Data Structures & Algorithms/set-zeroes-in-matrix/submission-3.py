class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #space: O(1)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
        #approach 2: space O(m+n)
        # ROWS = len(matrix)
        # COLS = len(matrix[0])
        # rows = [False]*ROWS
        # cols = [False]*COLS

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == 0:
        #             rows[r] = True
        #             cols[c] = True
                
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if rows[r] == True or cols[c] == True:
        #             matrix[r][c] = 0