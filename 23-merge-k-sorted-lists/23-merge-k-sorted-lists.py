# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergetwoll(h1=None, h2=None):
            head = ListNode()
            temp = head
            while h1 is not None and h2 is not None:
                if h1.val >= h2.val:
                    temp.next = h2
                    h2 = h2.next
                else:
                    temp.next = h1
                    h1 = h1.next
                temp = temp.next
            while h1 is not None:
                temp.next = h1
                h1 = h1.next
                temp = temp.next
            while h2 is not None:
                temp.next = h2
                h2 = h2.next
                temp = temp.next
            return head.next
        
        while len(lists) > 1:
            x = mergetwoll(lists[0], lists[1])
            lists.pop(1)
            lists.pop(0)
            lists.insert(0, x)
        if len(lists) == 1:
            return lists[0]
        else:
            return None