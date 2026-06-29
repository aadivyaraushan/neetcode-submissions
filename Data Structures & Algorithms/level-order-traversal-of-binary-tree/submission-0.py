# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = []

        visited = set()

        q.append(root)

        lists = []
        level_list = [] # stores all keys at a level

        if not root:
            return []

        while q:
            n = len(q) # size of one level. at any point at start of loop queue stores all nodes at a level.
            for i in range(n):
                front = q.pop(0)
                level_list.append(front.val)
                if front.left and front.left not in visited:
                    q.append(front.left)
                    visited.add(front.left)
                if front.right and front.right not in visited:
                    q.append(front.right)
                visited.add(front.right)
            lists.append(level_list)
            level_list = []
        return lists
            
        