# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        f_head = ListNode()
        s_head = ListNode()

        f_ptr = f_head
        s_ptr = s_head

        curr = head
        while curr:
            if curr.val < x:
                f_ptr.next = curr
                f_ptr = f_ptr.next
            else:
                s_ptr.next = curr
                s_ptr = s_ptr.next
            curr = curr.next
        s_ptr.next = None
        f_ptr.next = s_head.next

        return f_head.next
