# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root,x):
            if root is None:
                return 
            x.append(root.val)
            preorder(root.left,x)
            preorder(root.right,x)
            return x
        x = []
        return preorder(root,x)