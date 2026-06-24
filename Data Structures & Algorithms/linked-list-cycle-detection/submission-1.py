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
            if ptr.next != None:
                print(f"ptr.val = {ptr.val}, ptr.next.val = {ptr.next.val}")
            else:
                print(f"ptr.val = {ptr.val}. at end.")
            if ptr not in found:
                found.add(ptr)
            else:
                index = i
                break
            ptr = ptr.next
            i += 1

        return index != -1