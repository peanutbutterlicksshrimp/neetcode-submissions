# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        s = []
        d = {}
        node = root
        while node or s:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s[-1]
                if node.right and node.right not in d.keys():
                    node = node.right
                else:
                    node = s.pop()
                    l = d.get(node.left,0)
                    r = d.get(node.right, 0)
                    if abs(l-r) > 1:
                        return False
                    d[node] = 1 + max(l,r)
                    node = False
        return True
