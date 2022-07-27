# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = 0
        curr = head
        while curr: 
            l += 1
            curr = curr.next
        m = (l+1)//2
        curr = head
        while m>0:
            curr = curr.next
            m -= 1
        prev = None
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