# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, dct):
            if not node:
                return

            dct[node.val] = dct.get(node.val, 0)+1
            inorder(node.left, dct)
            inorder(node.right, dct)

        ctr = {}
        inorder(root, ctr)
        
        max_v = 0
        for v in ctr.values():
            if v > max_v:
                max_v = v
        
        ks = []
        for k,v in ctr.items():
            if v == max_v:
                ks.append(k)
        return ks
        

        
