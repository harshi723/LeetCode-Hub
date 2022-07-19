# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(root, maxv, minv):
            if not root: 
                return True
            elif minv >= root.val or maxv <= root.val:
                return False
            else:
                x = func(root.left, root.val, minv)
                y = func(root.right, maxv, root.val)
                return x and y
        return func(root, sys.maxsize, -sys.maxsize-1)