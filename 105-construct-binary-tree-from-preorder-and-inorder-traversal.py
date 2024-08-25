# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {value: idx for idx, value in enumerate(inorder)}        
        def helper(pre_start, pre_end, in_start, in_end):
            curr = preorder[pre_start]
            in_idx = inorder_map[curr]
            l_sub_len = in_idx - in_start
            r_sub_len = in_end - in_idx -1
            root = TreeNode(curr)
            if l_sub_len:
                root.left = helper(pre_start+1, pre_start+l_sub_len, in_start, in_idx)
            if r_sub_len:
                root.right = helper(pre_start+l_sub_len+1, pre_start+l_sub_len+r_sub_len, in_idx+1, in_end)
            return root
        return helper(0,len(preorder),0,len(inorder))
    
