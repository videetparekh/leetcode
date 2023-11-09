# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symm(a, b):
            if None not in (a,b):
                if a.val != b.val:
                    return False
            else:
                return a==b
            
            return symm(a.left, b.right) and symm(a.right, b.left)
        
        return symm(root.left, root.right)
