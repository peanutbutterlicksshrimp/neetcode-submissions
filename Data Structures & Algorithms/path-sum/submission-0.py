# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        def bt(root, s):
            if not root:
                return False
            s+=root.val
            path.append(root.val)
            print(path, " s: ", s)
            
            if not root.left and not root.right and s == targetSum:
                print("found")
                return True
            if bt(root.left, s):
                return True
            if bt(root.right,s):
                return True
            path.pop()
            return False
        return bt(root, 0)
