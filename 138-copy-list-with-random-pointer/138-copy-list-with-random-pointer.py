# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        l = {}
        newNode = Node(head.val)
        l[head] = newNode
        
        node = head
        while node:
            x = node.next
            if x:
                newNode = Node(x.val)
                l[x] = newNode
                l[node].next = newNode
            node = x
            
        node = head
        while node:
            x = node.random
            if x:
                l[node].random = l[node.random]
            node = node.next
        return l[head]
                
                
                
                
                
                