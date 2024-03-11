class Solution:
    def romanToInt(self, s: str) -> int:
        ri_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for i in range(len(s)-1):
            if s[i] == "I" and s[i+1] in ["V", "X"]:
                res-=1
            elif s[i] == "X" and s[i+1] in ["L", "C"]:
                res-=10
            elif s[i] == "C" and s[i+1] in ["D", "M"]:
                res-=100
            else:
                res+=ri_map[s[i]]
        
        res+=ri_map[s[-1]]
        return res
