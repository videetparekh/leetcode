class Solution:
    def numSquares(self, n: int) -> int:
        
        queue = deque([n])
        visited = set([n])

        lvl = 0
        qsize = 0
        while queue:
            if qsize == 0:
                qsize = len(queue)
                lvl+=1
            curr = queue.popleft()
            for i in range(1, int(curr**0.5)+1):
                rem = curr - (i*i)
                if rem == 0:
                    return lvl
                if rem not in visited:
                    queue.append(rem)
                    visited.add(rem)
            qsize-=1
        return lvl
