# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        temp = list3
        carry = 0
        while l1 or l2 or carry:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2: 
                s += l2.val
                l2 = l2.next
            s += carry
            carry = s//10
            node = ListNode(s%10)
            temp.next = node
            temp = temp.next
        return list3.next