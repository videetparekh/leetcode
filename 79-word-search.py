class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        n = len(board)
        m = len(board[0])

        def dfs(r, c, i):
            if len(word) == i:
                return True
            if (r < 0 or c < 0) or \
               (r >= n or c >= m) or \
               (board[r][c] != word[i]) or \
               (r,c) in path:
                return False
            
            path.add((r,c))
            res = dfs(r+1,c,i+1) or \
                  dfs(r-1,c,i+1) or \
                  dfs(r,c+1,i+1) or \
                  dfs(r,c-1,i+1)
            path.remove((r,c))

            return res

        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True
        return False
