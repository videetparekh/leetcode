# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        n=0

        e_start = ListNode(None, None)
        o_start = ListNode(None, None)

        curr = head
        e_curr = e_start
        o_curr = o_start

        while curr:
            if n%2==0:
                e_curr.next = curr
                e_curr = e_curr.next
                curr = curr.next
            else:
                o_curr.next = curr
                o_curr = o_curr.next
                curr = curr.next
            n+=1
        
        e_curr.next = o_start.next
        o_curr.next = None

        return e_start.next
