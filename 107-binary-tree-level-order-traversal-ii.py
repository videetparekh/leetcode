# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order = []

        queue = deque([(root, 0)])
        
        while queue:
            top, lvl = queue.popleft()
            if top:
                queue.append((top.left, lvl+1))
                queue.append((top.right, lvl+1))
                if len(level_order) <= lvl:
                    level_order.append([top.val])
                else:
                    level_order[lvl].append(top.val)
        
        return level_order[::-1]
