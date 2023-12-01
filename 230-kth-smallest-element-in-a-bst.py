# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        
        def inorder(node, target):
            if not node or len(nodes)>target:
                return

            inorder(node.left, target)
            nodes.append(node.val)
            inorder(node.right, target)

        inorder(root, k)
        return nodes[k-1]
