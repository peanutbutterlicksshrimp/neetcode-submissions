# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def bal(root):
            if not root:
                return 0
            lH = 0
            rH = 0
            lH = bal(root.left) 
            rH = bal(root.right)
            print("----------------")
            print("Root: ", root.val)
            print("lH: ", lH, " | RH: ", rH)
            print("rootHieght: ",lH + rH +1)
            print("----------------")
            rootHeight = max(lH,rH) +1
            if abs(rH - lH) > 1:
                return -10
            return rootHeight
        if not root:
            return True
        left=bal(root.left)
        right = bal(root.right)
        print("____FINAL__________")
        print("Root: ", root.val)
        print("lH: ", left, " | RH: ", right)
        print("----------------")
        if abs(left-right) > 1 or left < 0 or right < 0: 
            return False
        else:
            return True
        