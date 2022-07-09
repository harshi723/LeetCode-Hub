# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def path(root, targetSum):
            if root is None:
                return False
            if root.left == root.right == None:
                return True if root.val == targetSum else False
            x = path(root.left, targetSum - root.val)
            y = path(root.right, targetSum - root.val)
            return x or y
        return path(root, targetSum)