# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        x = []
        curr = head
        while curr:
            x.append(curr.val)
            curr = curr.next
        if k>=len(x): k %= len(x)
        if k==0: return head
        x[:] = x[len(x)-k:] + x[:len(x)-k]
        curr = head
        for i in x:
            curr.val = i
            curr = curr.next
        return head