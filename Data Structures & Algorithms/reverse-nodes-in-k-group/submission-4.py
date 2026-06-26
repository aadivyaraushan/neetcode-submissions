# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        group_prev = dummy

        def reverse_group(start_ptr, end_ptr):
            curr = start_ptr
            prev = end_ptr
            nex = start_ptr.next

            while nex != end_ptr:
                nex_next = nex.next

                curr.next = prev
                nex.next = curr

                prev = curr
                curr = nex
                nex = nex_next
            return curr, start_ptr  # new head, new tail

        while True:
            kth = group_prev

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            new_head, new_tail = reverse_group(group_prev.next, kth.next)
            
            group_prev.next = new_head
            group_prev = new_tail
            
        return head
        
