# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        rootCopy = root
        if not rootCopy:
            root = TreeNode(val)
            return root

        while rootCopy:
            if val > rootCopy.val:
                if rootCopy.right:
                    rootCopy = rootCopy.right
                else:
                    rootCopy.right = TreeNode(val)
                    break
            else:
                if rootCopy.left:
                    rootCopy = rootCopy.left
                else:
                    rootCopy.left = TreeNode(val)
                    break
        return root
        