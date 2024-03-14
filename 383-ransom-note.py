class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mmap=defaultdict(lambda: 0)
        for i in magazine:
            mmap[i]+=1
        
        for i in ransomNote:
            if mmap[i] == 0:
                return False
            mmap[i] -= 1
        
        return True
