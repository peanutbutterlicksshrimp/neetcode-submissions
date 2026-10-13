# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []
        node = root
        prev = None
        dep = {}
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or prev == node.right:
                    stack.pop()
                    left = dep.get(node.left,0)
                    right = dep.get(node.right, 0)
                    if abs(left - right) > 1:
                        return False
                
                    dep[node] = 1 + max(left,right)
                    prev = node
                    node = None
                else:
                    node = node.right
        return True