# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def h(root):
            if not root:
                return 0
            l = h(root.left)
            r = h(root.right)
            return max(l,r) +1

        if not root:
            return True
        l = h(root.left)
        r = h(root.right)
        if abs(l-r) > 1:
            return False
        lB = self.isBalanced(root.left)
        rB = self.isBalanced(root.right)
        return lB and rB
        
     