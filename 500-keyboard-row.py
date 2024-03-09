class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set("qwertyuiop")
        mid = set("asdfghjkl")
        bot = set("zxcvbnm")

        ret = []
        for word in words:
            tw = word.lower()
            if tw[0] in top and (not set(tw) - top):
                ret.append(word)
            elif tw[0] in mid and (not set(tw) - mid):
                ret.append(word)
            elif tw[0] in bot and (not set(tw) - bot):
                ret.append(word)
                
        return ret
