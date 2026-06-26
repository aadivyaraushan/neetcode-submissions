# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        total_list = []

        for l in lists:
            ptr = l

            while ptr != None:
                total_list.append(ptr.val)
                ptr = ptr.next
        
        print(f"total list: {total_list}")

        total_list.sort()

        new_list = None
        ptr = None
        for elem in total_list:
            if not new_list:
                new_list = ListNode(val=elem)
                ptr= new_list
            else:
                ptr.next = ListNode(val=elem)
                ptr = ptr.next
        
        return new_list
