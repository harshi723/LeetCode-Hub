# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        intersection = None
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                intersection = slow
                break
        if intersection is None: 
            return None
        slow = head
        while slow != intersection:
            slow = slow.next
            intersection = intersection.next
        return slow
            