# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        new_list = None

        # lenth coputation
        len_c = 0
        arr = []
        ptr = head
        while ptr != None:
            len_c += 1
            arr.append(ptr.val)
            ptr = ptr.next

        i = 0
        c = 1
        len_c -= 1
        
        head_og = head

        while i < len(arr): 
            # print(f"i: {i}, c: {c}, len_c: {len_c}")
            # if i is even, increment 0, 1, ... counter
            if i % 2 == 0:
                # print(f"i % 2 == 0 is true")
                # set current elem to c
                # print (f"so setting head.next = {arr[len_c]}")
                temp = head.next
                head.next = ListNode(val=arr[len_c])
                head.next.next = temp
                head = head.next
                # print(f"head now points to {head.val}")
                # increment c
                len_c -= 1
            else:
                # set current elem to len_c
                # print (f"i is odd so setting head.next = {arr[c]}")
                temp = head.next
                head.next = ListNode(val=arr[c])
                head.next.next = temp
                head = head.next
                # if head:
                    # print(f"head now points to {head.val}")

                # decrement len_C
                c += 1
            
            i += 1
        head = head_og
        start_i = len(arr)
        i = 0
        ptr = head
        while i < len(arr) * 2 and ptr:
            print(f"current ptr val: {ptr.val}")
            print(f"start_i: {start_i} vs i: {i}")
            if i >= start_i - 1:
                temp = ptr.next
                ptr.next = None
                ptr = temp
            else:
                ptr = ptr.next
            i += 1
        head = head_og
        