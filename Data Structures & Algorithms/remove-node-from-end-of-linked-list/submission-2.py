# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        ptr = head
        while ptr != None:
            length += 1
            ptr = ptr.next

        i_removal = length - n - 1
        # print(f"i_removal = {i_removal}")
        if i_removal < 0:
            head = head.next
            return head

        i = 0
        ptr = head
        while ptr != None:
            # print(f"ptr.val = {ptr.val}")
            if i == i_removal:
                # print(f"at removal index")
                # next elem is elem to remove
                temp = ptr.next.next
                # print(f"storing elem w val {temp.val} in temp")
                # edge case to deal w: what happens if ptr.next is null
                ptr.next = temp
                # if ptr:
                    # print(f"removed ptr.next and now ptr.val is {ptr.val}")
                i += 1
                # print(f"meanwhile i = {i} (with i_removal = {i_removal})")
            else:
                # print(f"i")
                i += 1
                ptr = ptr.next
        return head
