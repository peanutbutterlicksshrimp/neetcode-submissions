# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = deque([(root, targetSum - root.val)])
        
        while q:
            node, s = q.pop()
            if not node.left and not node.right and s == 0:
                return True
            
            if node.left:
                q.append((node.left, s - node.left.val))
            if node.right:
                q.append((node.right, s - node.right.val))
        return False