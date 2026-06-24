# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        found = set()

        index = -1
        ptr = head
        i = 0
        found_cycle = False
        while ptr != None:
            if ptr not in found:
                found.add(ptr)
            else:
                index = i
                break
            ptr = ptr.next
            i += 1

        return index != -1