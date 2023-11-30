class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                curr = grid[i][j]
                if i >= n or i <= 0 and not(j >= m or j <=0):
                    grid[i][j] = grid[i][j-1] + curr
                elif j >= m or j <=0 and not(i >= n or i <= 0):
                    grid[i][j] = grid[i-1][j] + curr
                elif i == 0 and j == 0:
                    pass
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + curr            
        return grid[n-1][m-1]
