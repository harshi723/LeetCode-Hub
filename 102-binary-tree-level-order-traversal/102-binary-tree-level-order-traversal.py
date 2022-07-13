# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = {}
        q = queue.Queue()
        if root: q.put((root,0))
        while not(q.empty()):
            node, lvl = q.get()
            l[lvl] = l.get(lvl, []) + [node.val]
            if node.left: q.put((node.left, lvl+1))
            if node.right: q.put((node.right, lvl+1))
        return l.values()