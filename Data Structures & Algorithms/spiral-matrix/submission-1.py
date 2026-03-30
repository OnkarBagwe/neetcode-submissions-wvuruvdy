class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0])
        res = []
        top = 0
        bottom = len(matrix)

        while l < r and top < bottom:
            #left to right
            for i in range(l,r):
                res.append(matrix[top][i])
            top += 1
            #top to bottm
            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1
            if not(l<r and top<bottom):
                break
            #right to left
            for i in range(r-1,l-1,-1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            #bottom to top
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][l])
            l += 1

        return res