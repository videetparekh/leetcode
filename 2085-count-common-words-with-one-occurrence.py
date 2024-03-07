class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        map1 = {}
        map2 = {}

        for word in words1:
            map1[word] = map1.get(word, 0)+1
        
        for word in words2:
            if word in map1.keys():
                map2[word] = map2.get(word, 0)+1
        
        return sum([1 for k in map2.keys() if map1[k]==1 and map2[k]==1])
