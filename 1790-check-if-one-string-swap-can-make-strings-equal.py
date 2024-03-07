class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mis_pairs = [[i,j] for i,j in zip(s1,s2) if i!=j]
        return (len(mis_pairs)==0 or (len(mis_pairs)==2 and 
            mis_pairs[0][0]==mis_pairs[1][1] and 
            mis_pairs[0][1]==mis_pairs[1][0]))
