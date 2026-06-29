# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # goal here is to create a list that contains all of the right-visible nodes

        # criteria possible:
        # 1. either its the right subchild and theres no other sub-child to its right on the same level
        # 2. or right subchild is null and its the left subchild and there's no sub-child to it right
        # 3. also, root is always included
        # ^ so this requires both sets for each level and predecessor map? 
        # acutally not it just requires level set just put right most of eahc elvel got it 

        q = []
        visited = set()
        level_set = []
        rv = []
        if not root:
            return []

        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                front = q.pop(0)
                level_set.append(front)

                if front.left and front.left not in visited:
                    visited.add(front.left)
                    q.append(front.left)
                if front.right not in visited and front.right:
                    visited.add(front.right)
                    q.append(front.right)
            rv.append(level_set[-1].val)
            level_set = []

        return rv

    