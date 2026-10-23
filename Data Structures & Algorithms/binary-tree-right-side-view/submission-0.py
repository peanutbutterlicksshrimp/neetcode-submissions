# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        lvl = 0
        if root:
            q.append(root)
            
    
        while len(q) > 0:
            print("lvl: ", lvl)
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            print("temp: ", temp)
            res.append(temp[0])

        return res
        