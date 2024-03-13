class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s) < 2:
            return s
            
        arr = [list() for i in range(numRows)]
        
        i = 0
        j = -1
        for char in s:
            arr[i].append(char)
            
            if i == 0:
                j = 1
            if i == numRows - 1:
                j = -1
            i+=j

        print(arr)
        return "".join(["".join(row) for row in arr])
