# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0

        if not head:
            return head
        
        node = head
        while node:
            n+=1
            node=node.next
        
        k=k%n

        if k==0:
            return head
        
        l=head
        r=head
        i=0
        while i<k:
            r=r.next
            i+=1

        while r.next:
            l=l.next
            r=r.next
        
        r.next = head
        head = l.next
        l.next = None

        return head
