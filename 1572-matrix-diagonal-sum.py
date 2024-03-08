class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        coords = set()
        n = len(mat)
        s = 0
        for i in range(n):
            s+= mat[i][i]
            coords.add((i,i))            
            if (i, n-1-i) not in coords:
                s+=mat[i][n-1-i]
        
        return s
            
