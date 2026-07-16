from collections import deque 

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        output = Node(val=node.val)
        cloned = {}

        def dfs(new_node, curr, origin):
            # print(f"calling dfs(new_node: {new_node.val}, curr: {curr.val}, origin: {origin.val})")
            # print(f"also, curr.neighbors = {[neighbor.val for neighbor in curr.neighbors]}")
            if len(curr.neighbors) == 0:
                return
            cloned[curr] = new_node

            for neighbor in curr.neighbors:
                if neighbor in cloned:
                    new_node.neighbors.append(cloned[neighbor])
                else:
                    # print(f"inspecting neighbor: {neighbor.val}")
                    new_neighbor = Node(val=neighbor.val)
                    new_node.neighbors.append(new_neighbor)
                    # print(f"made new neighbor with same val, added to new_node: {new_node.val}")
                    dfs(new_neighbor, neighbor, curr)
        
        cloned[node] = output
        for neighbor in node.neighbors:
            new_node = Node(val=neighbor.val)
            output.neighbors.append(new_node)
            dfs(new_node, neighbor, output)

        return output

                
            