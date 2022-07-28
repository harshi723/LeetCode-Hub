# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr: 
            nexts = curr.next
            curr.next = prev
            prev = curr
            curr = nexts
        while prev:
            if prev.val!=head.val: return False
            else: 
                prev = prev.next
                head = head.next
        return True