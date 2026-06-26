# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ptr = None

        merged_list = ListNode()
        merged_list_ptr = merged_list
        
        while True:
            min_node_index = -1

            for i, head_elem in enumerate(lists):
                if not lists[i]:
                    continue
                if min_node_index == -1 or lists[min_node_index].val > head_elem.val:
                    min_node_index = i
                
            
            if min_node_index == -1:
                break

            merged_list_ptr.next = lists[min_node_index]
            lists[min_node_index] = lists[min_node_index].next
            merged_list_ptr = merged_list_ptr.next
        
        return merged_list.next




