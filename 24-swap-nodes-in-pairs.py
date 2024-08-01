# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Create a temporary node to point to head. Create a pointer at head, and a pointer at head.next
        tmp = ListNode(None, head)
        start = tmp
        p1 = head
        p2 = p1.next

        
        while p1 and p2:
            # P1 points to P2.next, P2 points to P1, tmp points to P2.
            p1.next = p2.next
            p2.next = p1
            tmp.next = p2

            # Order is now tmp, p2, p1. Swap p1, p2 to maintain tmp, p1, p2.
            p1, p2 = p2, p1

            # If there are at least two more elements in the List, move all pointers up by 2
            if p2.next and p2.next.next:
                for _ in range(2):
                    tmp = tmp.next
                    p1 = p1.next
                    p2 = p2.next
            else:
                break
        
        # Return head
        return start.next
