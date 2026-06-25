"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def print_list(self, head):
        ptr = head
        elems = []
        while ptr != None:
            elems.append(f"{ptr.val}")
            ptr = ptr.next
        return " -> ".join(elems)
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = None
        copy_ptr = copy

        old_to_copy = {}

        ptr = head
        while ptr != None:
            # print("values at start of iteration")
            # if copy_ptr:
                # print(f"copy_ptr.val: {copy_ptr.val}")
            # if ptr:
                # print(f"ptr.val: {ptr.val}")
            # if ptr.random:
                # print(f"ptr.random.val: {ptr.random.val}")
            if copy == None:
                copy = Node(ptr.val, ptr.next, ptr.random)
                old_to_copy[ptr] = copy
                copy_ptr = copy
            else:
                copy_ptr.next = Node(ptr.val, ptr.next, ptr.random)
                copy_ptr = copy_ptr.next
                old_to_copy[ptr] = copy_ptr
            ptr = ptr.next
        
        # print(f"old_to_copy: {old_to_copy}")
        copy_ptr = copy
        ptr = head
        while copy_ptr != None:
            if ptr.random:
                # print(f"ptr.random.val = {ptr.random.val}")
                copy_ptr.random = old_to_copy[ptr.random]

            ptr = ptr.next
            copy_ptr = copy_ptr.next

        print(f"old list: {self.print_list(head)}")
        print(f"new list: {self.print_list(copy)}")
        return copy