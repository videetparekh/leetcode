class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")":"(", "]":"[", "}":"{"}
        stk = []
        for char in s:
            if char in mp:
                if not stk or stk.pop() != mp[char]:
                    return False
            else:
                stk.append(char)
        return len(stk) == 0
