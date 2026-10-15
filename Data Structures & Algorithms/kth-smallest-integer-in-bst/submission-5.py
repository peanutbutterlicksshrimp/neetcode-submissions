# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrdPred(root, curr):
            while root and root.right and root.right != curr:
                root = root.right
            return root
        curr = root
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                node = inOrdPred(curr.left, curr)
                if not node.right:
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    k-=1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1