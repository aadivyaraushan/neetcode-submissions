# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        output = None
        output_ptr = output
        carry_over = 0

        while ptr1 != None or ptr2 != None:
            
            new_num = 0

            # invariant: ptr1, ptr2 should go term by term through both nums
            
            # both are non null
            sum_val = 0
            if ptr1 == None:
                sum_val = ptr2.val + carry_over
            elif ptr2 == None:
                sum_val = ptr1.val + carry_over
            else:
                # print(f"at current iter, ptr1.val = {ptr1.val} and ptr2.val = {ptr2.val}")
                sum_val = ptr1.val + ptr2.val + carry_over
            # invariant: this should calculate sum correcly
            # print(f"from those values, sum_val = {sum_val}")
            carry_over = 0

            first_digit = sum_val // 10
            second_digit = sum_val % 10
            new_num = second_digit 
            # invariant: this should correctly compute firsta nd sec digit
            # and work for single and double digit nums
            # print(f"from that sum, first_digit = {first_digit} and second_digit = {second_digit}")
            carry_over += first_digit

            # invariant: carry_over should always store the right carry over at each point
            # print(f"now, carry_over = {carry_over}")
            
            if output == None:
                output = ListNode(val=new_num)
                output_ptr = output
            else:
                output_ptr.next = ListNode(val=new_num)
                output_ptr = output_ptr.next
            if ptr1:
                ptr1 = ptr1.next
            if ptr2:
                ptr2 = ptr2.next
            # print(f"\n")
        
        if carry_over != 0:
            output_end = None
            ptr = output
            while ptr.next != None:
                ptr = ptr.next
            output_end = ptr
            output_end.next = ListNode(val=carry_over)

        return output