# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def small(root,count):
            if not root:
                return [True, 0]
            left = small(root.left,count)
            # print("root: ", root.val, " | l: ", left)
            # print("Compare: L: ", left[1], "| count: ", count)
            count = max(left[1],count) + 1
            # print("root: ", root.val, " } c: ", count)
            if not left[0]:
                return left
            elif k == count:
                # print("found: ", root.val, " } c: ", count)
                return [False, root.val]
            else:
                # print("RIGHT")
                right = small(root.right,count)
                # count = max(right[1],count) + 1
                # print("test is false: ", right)
                if not right[0]: 
                    return right
                return [right[0], max(count,right[1])]
        res = small(root,0)
        # print(res[1])
        return res[1]



