# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        x = []
        if root is None: return x
        q = queue.Queue()
        q.put(root)
        q.put('null')
        y = []
        while not q.empty():
            curr = q.get()
            if curr == 'null':
                x.append(y)
                y = []
                if q.empty(): 
                    break
                q.put('null')
            else:
                y.append(curr.val)
                if curr.left: q.put(curr.left)
                if curr.right: q.put(curr.right)
        return x