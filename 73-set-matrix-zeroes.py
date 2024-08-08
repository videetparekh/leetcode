class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        row_zeros = set()
        col_zeros = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_zeros.add(i)
                    col_zeros.add(j)
        
        
        for i in range(n):
            for j in range(m):
                if i in row_zeros or j in col_zeros:
                    matrix[i][j] = 0
