# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ptr = head
        while ptr != None:
            stack.insert(0, ptr.val)
            ptr = ptr.next
        print(f"generated stack: {stack}")
        if not stack:
            return None
        new_list = ListNode()
        ptr = new_list
        while stack:
            elem = stack.pop(0)
            ptr.val = elem
            if stack:
                ptr.next = ListNode()
                ptr = ptr.next
        return new_list