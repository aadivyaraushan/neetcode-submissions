# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        ptr1 = list1
        ptr2 = list2
        merged = None
        ptr3 = merged

        while ptr1 != None and ptr2 != None:
            if ptr1.val <= ptr2.val:
                if merged is None:
                    merged = ListNode(val=ptr1.val)
                    ptr3 = merged
                else:
                    ptr3.next = ListNode(val=ptr1.val)
                    ptr3 = ptr3.next
                ptr1 = ptr1.next
            else:
                if merged is None:
                    merged = ListNode(val=ptr2.val)
                    ptr3 = merged
                else:
                    ptr3.next = ListNode(val=ptr2.val)
                    ptr3 = ptr3.next

                ptr2 = ptr2.next
            print(f"ptr3 is now {ptr3.val}")
            if ptr1:
                print(f"ptr1.val = {ptr1.val} now")
            if ptr2:
                print(f"ptr2.val = {ptr2.val} now")
        
        if ptr1 == None and ptr2 != None:
            while ptr2:
                ptr3.next = ListNode(ptr2.val)
                ptr3 = ptr3.next
                ptr2 = ptr2.next
        elif ptr1 != None and ptr2 == None:
            while ptr1:
                ptr3.next = ListNode(ptr1.val)
                ptr3 = ptr3.next
                ptr1 = ptr1.next

        return merged
