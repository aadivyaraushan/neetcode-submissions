# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head
        output = None
        output_ptr = None

        while slow_ptr and fast_ptr:
            for i in range(k):
                if fast_ptr == None:
                    break
                fast_ptr = fast_ptr.next
            if slow_ptr == None:
                break

            prev = None
            curr = slow_ptr
            next_node = slow_ptr.next
            stack = []
            while slow_ptr != fast_ptr:
                stack.append(slow_ptr.val)
                slow_ptr = slow_ptr.next
            # print(f"stack made: {stack}")
            if len(stack) == k:
                queue_new = deque()

                while stack:
                    elem = stack.pop()
                    queue_new.appendleft(elem)
                
                print(f"new queue: {queue_new}")
                while queue_new:
                    stack.append(queue_new.pop())
            for elem in stack:
                if not output:
                    output = ListNode(val=elem)
                    output_ptr = output
                else:
                    output_ptr.next = ListNode(val=elem)
                    output_ptr = output_ptr.next
            
        return output
        
