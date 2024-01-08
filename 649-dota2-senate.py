from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = deque()
        dire = deque()
        n = len(senate)

        for i, sen in enumerate(senate):
            if sen == "R":
                rad.append(i)
            else:
                dire.append(i)
        
        while len(rad) > 0 and len(dire) > 0:
            r = rad.popleft()
            d = dire.popleft()

            if r < d:
                rad.append(r+n)
            else:
                dire.append(d+n)

        return "Radiant" if len(dire) == 0 else "Dire"  
