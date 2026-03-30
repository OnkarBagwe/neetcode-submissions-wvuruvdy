class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(r-l):
                top = l
                bottom = r

                #topleft
                topleft = matrix[top][l+i]

                #bottom left to top left
                matrix[top][l+i] = matrix[bottom-i][l]

                #bottom right to bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                #top right to bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #top left to top right
                matrix[top+i][r] = topleft

            l += 1
            r -= 1