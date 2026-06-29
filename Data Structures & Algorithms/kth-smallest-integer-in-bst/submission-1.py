# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []

        visited = set()
        visited_vals = []

        q.append(root)
        visited.add(root)
        visited_vals.append(root.val)

        while q:
            front = q.pop(0)

            if front.left and front.left not in visited:
                visited.add(front.left)
                visited_vals.append(front.left.val)
                q.append(front.left)
            if front.right and front.right not in visited:
                visited.add(front.right)
                visited_vals.append(front.right.val)
                q.append(front.right)
        

        nodes = sorted(visited_vals)
        return nodes[k-1]       