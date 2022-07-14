class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(grid2, i2, j2):
            if i2<0 or j2<0 or i2>=len(grid2) or j2>=len(grid2[0]):
                return 0
            
            if grid2[i2][j2] == 0:
                return 0
            
            grid2[i2][j2] = 0
            if grid1[i2][j2] == 0:
                dfs(grid2, i2+1, j2)
                dfs(grid2, i2-1, j2)
                dfs(grid2, i2, j2+1)
                dfs(grid2, i2, j2-1)
                return -1
            elif grid1[i2][j2] == 1:
                return dfs(grid2, i2+1, j2)+dfs(grid2, i2-1, j2)+dfs(grid2, i2, j2+1)+dfs(grid2, i2, j2-1)
            
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1:
                    tmp = dfs(grid2, i, j)
                    if tmp >= 0:
                        count += 1
                    
        return count