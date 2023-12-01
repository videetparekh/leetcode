class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_len = min([len(s)  for s in strs])
        lcprefix = ""
        i = 0
        while i < min_len:
            chars = set([s[i] for s in strs])
            if len(chars) != 1:
                break
            lcprefix += list(chars)[0]
            i+=1
        return lcprefix
