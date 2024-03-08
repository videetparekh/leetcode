class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        c_ones = -1
        c_zeros = -1

        if len(s) == 0:
            return False

        is_ones = s[0]=="1"
        ctr = 0

        for i in s:
            if i == "1":
                if is_ones:
                    ctr+=1
                else:
                    is_ones = True
                    ctr = 1
                if ctr > c_ones:
                    c_ones = ctr
            if i == "0":
                if not is_ones:
                    ctr+=1
                else:
                    is_ones = False
                    ctr = 1
                if ctr > c_zeros:
                    c_zeros = ctr
        return c_ones > c_zeros
                
