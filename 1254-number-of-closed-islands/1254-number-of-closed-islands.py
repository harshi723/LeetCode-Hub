class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def island(grid,r,c):
            if grid[r][c] == 1:
                return True
            
            if r<=0 or c<=0 or r>=len(grid)-1 or c>=len(grid[0])-1:
                return False
            
            grid[r][c] = 1
            a1 = island(grid,r-1,c)
            a2 = island(grid,r+1,c)
            a3 = island(grid,r,c-1)
            a4 = island(grid,r,c+1)
            return a1 and a2 and a3 and a4
        
        l = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                if grid[i][j] == 0 and island(grid, i, j):
                    l += 1
        return l