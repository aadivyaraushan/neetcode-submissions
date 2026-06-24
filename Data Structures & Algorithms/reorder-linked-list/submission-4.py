# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def print_list(self, head):
        curr = head
        vals = []
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        output = " -> ".join(vals)
        return output

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast_ptr = head
        slow_ptr = head
        slow_ptr_prev = None
        
        while fast_ptr != None and fast_ptr.next != None:
            # print(f"currently slow_ptr.val = {slow_ptr.val}")
            # print(f"currently fast_ptr.val = {fast_ptr.val}")
            slow_ptr_prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        if slow_ptr_prev is not None:
            slow_ptr_prev.next = None

        print(f"second half: {self.print_list(slow_ptr)}")

        ptr = slow_ptr
        prev = None
        while ptr != None:
            next_node = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = next_node
        slow_ptr = prev
        
        print(f"second half reversed: {self.print_list(slow_ptr)}")
        print(f"first half: {self.print_list(head)}")

        # now slow_ptr would point at mid of array
        ptr = head
        while ptr != None:
            next_node = ptr.next
            next_slow_ptr = slow_ptr.next

            ptr.next = slow_ptr
            slow_ptr.next = next_node
            
            slow_ptr = next_slow_ptr
            ptr = next_node
        print(f"final list: {self.print_list(head)}")
        print(f"final_prev: {self.print_list(prev)}")
        print(f"final rev part: {self.print_list(slow_ptr)}")
        if slow_ptr is not None:
            ptr_end = head
            while ptr_end.next != None:
                ptr_end = ptr_end.next

            ptr_end.next = slow_ptr
            


            
        