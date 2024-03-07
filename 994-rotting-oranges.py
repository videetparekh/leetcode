class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def rot(i,j,n,m,grid,addval):
            grid[i][j] = addval

            if i > 0 and (grid[i-1][j]==1 or grid[i-1][j] > 1 + addval):
                rot(i-1,j,n,m,grid,addval+1)
            if i < n-1 and (grid[i+1][j]==1 or grid[i+1][j] > 1 + addval):
                rot(i+1,j,n,m,grid,addval+1)
            if j > 0 and (grid[i][j-1]==1 or grid[i][j-1] > 1 + addval):
                rot(i,j-1,n,m,grid,addval+1)
            if j < m-1 and (grid[i][j+1]==1 or grid[i][j+1] > 1 + addval):
                rot(i,j+1,n,m,grid,addval+1)

        
        n=len(grid)
        m=len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rot(i,j,n,m,grid,2)

        maxval = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                else:
                    maxval = max(grid[i][j], maxval)

        return maxval-2
