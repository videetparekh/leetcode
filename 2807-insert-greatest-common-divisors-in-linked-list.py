# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def calculate_gcd(x, y):
            while(y):
                x, y = y, x % y
            return x
        
        if not head or not head.next:
            return head
        
        startp = head
        nextp = startp.next
        while nextp is not None:
            gcd = calculate_gcd(startp.val, nextp.val)
            gcd_node = ListNode(gcd, nextp)
            startp.next = gcd_node
            startp = nextp
            nextp = nextp.next
        
        return head
