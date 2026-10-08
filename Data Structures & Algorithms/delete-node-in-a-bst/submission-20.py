# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        copy = root
        par = None
        while copy and copy.val != key:
            par = copy
            if key > copy.val:
                copy = copy.right
            else:
                copy = copy.left
        if not copy:
            return root
        if copy.left and copy.right:
            curr = copy.right
            parent = None
            while curr and curr.left:
                parent = curr
                curr = curr.left
            if not parent: #if we need to delete root
                copy.val = copy.right.val
                copy.right = copy.right.right
            else:
                copy.val = curr.val
                parent.left = curr.right
        elif not copy.left and not copy.right:
            if not par:
                return None
            if key > par.val:
                par.right = None
            elif key < par.val:
                par.left = None
        elif not copy.left:
            if not par:
                return copy.right
            if key > par.val:
                par.right = copy.right
            else:
                par.left = copy.right
        else:
            if not par:
                return copy.left
            if key > par.val:
                par.right = copy.left
            else:
                par.left = copy.left
        return root
