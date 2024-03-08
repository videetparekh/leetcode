class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        new_s = [""]*len(s)
        for i in s:
            new_s[int(i[-1])-1] = i[:-1]
        return " ".join(new_s)
