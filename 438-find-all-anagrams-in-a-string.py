from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if not (s and p) or len(s) < len(p):
            return res

        letctr = Counter(p)
        l, r = 0, len(p)
        currctr = Counter(s[l:r])
        
        while r <= len(s):
            if currctr == letctr:
                res.append(l)
            currctr[s[l]] -= 1
            if r < len(s):
                currctr[s[r]] = currctr.get(s[r], 0) + 1
            l += 1
            r += 1
        return res

        

