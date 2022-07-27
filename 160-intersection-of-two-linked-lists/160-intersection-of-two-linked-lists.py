# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # l = {}
        # while headA:
        #     l[headA] = headA.next
        #     headA = headA.next
        # while headB:
        #     if headB in l: return headB
        #     else: headB = headB.next
        # return None
        listA, listB = headA, headB
        while listA != listB:
            listA = headB if not listA else listA.next
            listB = headA if not listB else listB.next
        return listA