# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        x = []
        curr = head
        while curr:
            x.append(curr)
            curr = curr.next
        for i in range(len(x)//2):
            temp = x[i].next
            x[i].next = x[len(x)-1-i]
            x[len(x)-1-i].next = temp
        x[len(x)//2].next = None
        