"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        x = []
        self.preorderHelper(root, x)
        return x
    
    def preorderHelper(self, root, x):
        if root == None:
            return
        x.append(root.val)
        for i in root.children:
            self.preorderHelper(i, x)
                