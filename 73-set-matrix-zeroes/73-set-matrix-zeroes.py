class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        x = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x.append([i,j])
        if len(x):
            for i in x:
                matrix[i[0]] = [0]*n
            for i in matrix:
                for j in x:
                    i[j[1]] = 0