# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root, lvl):
            if not root:
                return None
            while len(res) <= lvl:
                res.append(-1)
            if res[lvl] == -1:
                res[lvl] = root.val
            if root.right:
                dfs(root.right, lvl + 1)
            if root.left:
                dfs(root.left, lvl + 1)
        dfs(root,0)
        return res
            
