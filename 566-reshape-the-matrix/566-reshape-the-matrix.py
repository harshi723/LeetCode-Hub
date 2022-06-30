class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        
        a = []
        for i in mat:
            for j in i:
                a.append(j)
                
        l = [[0 for i in range(c)] for i in range(r)]
        k = 0
        
        for i in range(r):
            for j in range(c):
                l[i][j] = a[k]
                k += 1
        return l