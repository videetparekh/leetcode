class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dct = {x[0]: x for x in pieces}

        res = []
        for num in arr:
            if num in dct:
                res.extend(dct[num])
        
        return res == arr
