class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x.append((i,j))
        # print(x)
        for num in x:
            r,c = num[0],num[1]
            for i in range(len(matrix)):
                matrix[i][c] = 0
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
                    
                