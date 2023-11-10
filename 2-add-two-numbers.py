class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)
        curr = start

        overhead = 0
        n1 = l1
        n2 = l2
        while (n1 is not None or n2 is not None or overhead != 0):
            l1_value = n1.val if n1 else 0
            l2_value = n2.val if n2 else 0
            total = l1_value + l2_value + overhead
            curr.next = ListNode(total % 10)
            overhead = total // 10
            
            n1 = n1.next if n1 else n1
            n2 = n2.next if n2 else n2
            curr = curr.next
    
        return start.next
