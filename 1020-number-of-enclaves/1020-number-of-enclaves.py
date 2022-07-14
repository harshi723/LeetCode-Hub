class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def connected(grid,r,c):
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 1:
                grid[r][c] = 0
                connected(grid,r-1,c)
                connected(grid, r+1,c)
                connected(grid,r,c-1)
                connected(grid,r,c+1)
        
        for i in range(len(grid)):
            connected(grid,i,0)
            connected(grid,i,len(grid[0])-1)
            for j in range(len(grid[0])):
                connected(grid,0,j)
                connected(grid,len(grid)-1,j)
        
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    c += 1
        return c