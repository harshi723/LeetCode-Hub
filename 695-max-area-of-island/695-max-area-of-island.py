class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(grid,r,c):
            if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c] == 1:
                grid[r][c] = 'v'
                self.l += 1
                area(grid,r-1,c)
                area(grid,r+1,c)
                area(grid,r,c-1)
                area(grid,r,c+1)
                return self.l
        
        m = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.l = 0
                    x = area(grid,i,j)
                    m = max(m,x)
        return m