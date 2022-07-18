class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = col = res = 0
        bcol = len(mat)-1
        for i in range(len(mat)):
            x = mat[row][col]
            y = mat[row][bcol]
            if col==bcol:
                res += x
            else:
                res += x+y
            row += 1
            col += 1
            bcol -= 1
        return res