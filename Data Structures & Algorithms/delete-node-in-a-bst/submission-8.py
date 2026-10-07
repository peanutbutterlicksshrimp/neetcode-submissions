# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        copy = root
        parent = None
        while copy and copy.val != key:
            if key > copy.val:
                #go right
                parent = copy
                copy = copy.right
            elif key < copy.val:
                #go left
                parent = copy
                copy = copy.left
        if not copy:
            return root

        if not copy.left: #one right
            if not parent:
                return copy.right
            if key > parent.val:
                parent.right = copy.right
            else:
                parent.left = copy.right
        elif not copy.right: #one left
            if not parent:
                return copy.left
            if key > parent.val:
                parent.right = copy.left
            else:
                parent.left = copy.right
        else:    
                #both children or no children
            par = None # parent of right subtree min node
            cur = copy.right
            nodeDelete = copy
            while cur and cur.left:
                par = cur
                cur = cur.left
            #if there was a left traversal:
            if par:
                par.left = cur.right
                cur.right = nodeDelete.right
            cur.left = nodeDelete.left
                
            #if we are deleting root:
            if not parent:
                return cur
                
            if parent.left == nodeDelete:
                parent.left = cur
            else:
                parent.right = cur
        return root




