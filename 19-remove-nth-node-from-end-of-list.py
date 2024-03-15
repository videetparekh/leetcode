# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next and n==1:
            return None 

        dummy = ListNode(None, head)
        lptr = dummy
        rptr = dummy

        for _ in range(n+1):
            rptr = rptr.next
        
        while rptr:
            rptr = rptr.next
            lptr = lptr.next
        
        lptr.next = lptr.next.next
        return dummy.next
