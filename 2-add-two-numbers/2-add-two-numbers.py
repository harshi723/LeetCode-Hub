# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c = 0
        p = None
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            res = x+y+c
            c = res//10
            temp = ListNode(res%10)
            if p == None:
                p = temp
                curr = temp
            else:
                curr.next = temp
                curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if c: curr.next = ListNode(c)
        return p