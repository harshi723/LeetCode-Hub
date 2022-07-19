class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        ans = [[0 for i in range(c)] for j in range(r)]
        for i in range(m):
            for j in range(n):
                x = n*i+j
                ans[x//c][x%c] = mat[i][j]
        return ans