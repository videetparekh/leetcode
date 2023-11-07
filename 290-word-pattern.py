class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hashmap = {}

        s = s.split(" ")
        if len(set(pattern)) != len(set(s)):
            return False
        if len(pattern) != len(s):
            return False
        for i, j in zip(pattern, s):
            if i in hashmap and j != hashmap[i]:
                return False
            else:
                hashmap[i] = j
        return True
