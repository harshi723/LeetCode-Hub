# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr is not None:
            length += 1            
            curr = curr.next
        i = length - n 
        if i == 0:
            head = head.next
        else:
            temp = head
            i -= 1
            while i > 0:
                temp = temp.next
                i -= 1
            temp.next = temp.next.next
        return head