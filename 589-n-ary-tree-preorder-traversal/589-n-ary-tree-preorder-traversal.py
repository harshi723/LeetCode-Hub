"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def helper(root, x):
            if not root: return 
            x.append(root.val)
            for i in root.children:
                helper(i,x)
            return x
        x = []
        return helper(root,x)