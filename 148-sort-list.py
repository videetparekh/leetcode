# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        lst = []
        node = head
        while node:
            lst.append((node.val, node))
            node = node.next
        
        lst.sort(key=lambda x: x[0])

        start = ListNode(None, None)
        node = start
        for i in range(len(lst)):
            node.next = lst[i][1]
            node = node.next

        node.next = None
        return start.next


