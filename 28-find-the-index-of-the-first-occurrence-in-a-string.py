class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)

        i, j = 0, 0

        while i < h-n+1 and j < h:
            if haystack[j] == needle[j-i]:
                j+=1
            else:
                i+=1
                j = i
            if j-i == n:
                return i
        return -1 




