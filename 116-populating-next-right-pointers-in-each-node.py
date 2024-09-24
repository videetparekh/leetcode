"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        queue = deque([(root, 0)])
        prev = None
        prev_lvl = -1
        while queue:
            node, lvl = queue.popleft()
            if node:
                if prev and prev_lvl == lvl:
                    prev.next = node
                prev = node
                prev_lvl = lvl
                queue.append((node.left, lvl+1))
                queue.append((node.right, lvl+1))
        return root
