# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        curr = head
        while curr is not None:
            l += 1
            curr = curr.next
        m = l//2 
        while m:
            head = head.next
            m -= 1
        return head
        