class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = False
        ptr = -1
        for i in range(len(s)-1, -1, -1):
            if s[i].isalnum() and not start:
                start = True
                ptr = i
            if s[i] == " " and start:
                return ptr-i
        
        if start is False:
            return 0
        
        if start is True:
            return ptr+1


        
