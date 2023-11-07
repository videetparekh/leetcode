class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = 0
        neg = False
        
        if len(s) == 0:
            return 0

        if s[0] in ["-", "+"]:
            neg = s[0] == "-"
            s = s[1:]
        
        for i in s:
            if not i.isdigit():
                break
            num*=10
            num+=int(i)
        
        if neg:
            num*=-1
        
        num = min(num, 2 ** 31 - 1)
        num = max(-(2 ** 31), num)
        
        return num
        
