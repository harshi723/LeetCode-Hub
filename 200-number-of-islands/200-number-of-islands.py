class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        c = 0
        def island(r,c, grid):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '1':
                grid[r][c] = -1
                island(r,c+1,grid)
                island(r,c-1,grid)
                island(r+1,c,grid)
                island(r-1,c, grid)
                return
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island(i,j, grid)
                    c += 1
        return c