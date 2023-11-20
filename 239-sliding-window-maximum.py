from collections import deque
from copy import copy
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = deque([nums[0]])
        op = []
        for i in nums[1:k]:
            while len(window) > 0 and window[-1] < i:
                window.pop()
            window.append(i)
        op.append(window[0])
        
        for i in range(k,n):
            lval = nums[i-k]
            if window[0] == lval:
                window.popleft()
            while len(window) > 0 and window[-1] < nums[i]:
                window.pop()
            window.append(nums[i])
            op.append(window[0])
        return op
