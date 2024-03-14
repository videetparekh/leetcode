class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        
        l, r, lss = 0, 0, 0
        n = len(s)
        while r < n:
            if s[r] in chars:
                chars.remove(s[l])
                l+=1
            else:
                chars.add(s[r])
                lss = max(lss, r-l+1)
                r+=1
        return lss
        
