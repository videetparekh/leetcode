class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        if n < 0:
            return 0
        m = len(grid[0])
        if m < 0:
            return 0
        
        def delete_island(grid, i, j, n, m):
            stack = [(i,j)]
            while stack:
                x,y = stack.pop()
                if x>=0 and x<n and y>=0 and y <m and grid[x][y] == "1":
                    grid[x][y] = "0"
                    stack.append((x-1,y))
                    stack.append((x+1,y))
                    stack.append((x,y-1))
                    stack.append((x,y+1))


        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands+=1
                    delete_island(grid,i,j,n,m)
        
        return islands
