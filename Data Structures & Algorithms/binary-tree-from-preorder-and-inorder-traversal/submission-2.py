# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        j = 0
        i = 0
        n = len(preorder)
        head = TreeNode(None)
        curr = head
        
        while j < n and i < n:
            node = TreeNode(preorder[i], right = curr.right)
            curr.right = node
            curr = curr.right
            i+=1
            while i < n and inorder[j] != curr.val:
                curr.left = TreeNode(preorder[i], right = curr)
                curr = curr.left
                i+=1
            j+=1
            while curr.right and j < n and inorder[j] == curr.right.val:
                parent = curr.right
                curr.right = None
                curr = parent
                j+=1
        return head.right

