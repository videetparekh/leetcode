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
            return None
        ptrs = {}

        def dfs(node, depth):
            if node:
                if depth in ptrs:
                    ptrs[depth].next = node
                ptrs[depth] = node
            
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        
        dfs(root, 0)
        return root
