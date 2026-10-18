# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        m = {}
        for i, val in enumerate(inorder):
            m[val] = i
        pre_idx = 0
        def build(left, right):
            nonlocal pre_idx
            if left > right:
                return None
            
            root = preorder[pre_idx]
            node = TreeNode(root)
            pre_idx +=1

            inord_idx = m[root]
            node.left = build(left, inord_idx -1)
            node.right = build(inord_idx + 1, right)
            return node

        root = build(0, len(preorder)-1)
        return root


