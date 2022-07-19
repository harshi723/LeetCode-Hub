class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def zeroIt(matrix, i, j):
            for m in range(len(matrix)):
                if matrix[m][j] != 'X':
                    matrix[m][j] = 0
            for m in range(len(matrix[0])):
                if matrix[i][m] != 'X':
                    matrix[i][m] = 0
        
        x = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = 'X'
        # print(x)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'X':
                    zeroIt(matrix, i, j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'X':
                    matrix[i][j]= 0
                
                