# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        l = 0
        while curr: 
            curr = curr.next
            l += 1
        index = l-n-1
        if index==-1: return head.next
        curr = head
        while index>0:
            curr = curr.next
            index -= 1
        curr.next = curr.next.next
        return head
        
        