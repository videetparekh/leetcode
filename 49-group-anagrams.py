class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        op_dct = defaultdict(list)

        for i in strs:
            sortstr = ''.join(sorted(i))
            op_dct[sortstr].append(i)
        return op_dct.values()
