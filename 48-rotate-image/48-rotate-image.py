class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        t, b, n = 0, len(matrix)-1, len(matrix)        
        while t<b:
            x = []

            for i in range(n):
                x.append(matrix[t][t+i])
            for i in range(n):
                matrix[t][b-i] = matrix[t+i][t]
            for i in range(n):
                matrix[t+i][t] = matrix[b][t+i]
            for i in range(n):
                matrix[b][t+i] = matrix[b-i][b]
            for i in range(n):
                matrix[t+i][b] = x[i]
            t+=1
            b-=1
            n -=2