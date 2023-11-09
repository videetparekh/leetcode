"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        que = deque([(root, 0)])

        curr = Node()
        curr_lvl = 0
        while que:
            node, lvl = que.pop()
            if node:
                que.appendleft((node.left, lvl+1))
                que.appendleft((node.right, lvl+1))

                if curr_lvl != lvl:
                    curr_lvl = lvl
                    curr = Node()
                
                curr.next = node
                curr = node
        return root
            
            
