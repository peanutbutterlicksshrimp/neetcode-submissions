# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []
        
        def dfs(root,level, arr):
            if not root:
                return None
            i = len(arr)
            while i == level:
                arr.append([])
                i+=1
            arr[level].append(root.val)
            #print("this is the map after: ", arr)

            if root.left:
                dfs(root.left, level+1, arr)
            if root.right:
                dfs(root.right, level+1, arr)
        dfs(root,0, arr)
        return arr
            
        