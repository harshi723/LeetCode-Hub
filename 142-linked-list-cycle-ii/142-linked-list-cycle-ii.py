# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        flag = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                flag = 0
                break
        if flag: return None
        while head!=slow:
            head = head.next
            slow = slow.next
        return slow