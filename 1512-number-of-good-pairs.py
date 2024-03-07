class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dct={}
        sum=0

        for i in nums:
            dct[i]=dct.get(i, 0) + 1

        for k,v in dct.items():
            if v>1:
                # E.g. v=4. 1 can form pairs with 2,3,4 (3 pairs). 
                # 2 can form pairs with 3,4 (2 pairs).
                # 3 can form a pair with 4 (1 pair).
                # 1 + 2 + 3 + ... v-1 pairs. 
                sum=sum+(v*(v-1))/2
        return(int(sum))
