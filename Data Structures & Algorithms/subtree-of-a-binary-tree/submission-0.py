# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = [root]
        visited = set()

        # c = 0

        def equalTrees(root1, root2):
            if not root1 and not root2:
                return True
            if not root1:
                return False
            if not root2:
                return False
            if root1.val != root2.val:
                return False
            return equalTrees(root1.left, root2.left) and equalTrees(root1.right, root2.right)

        while q:
            # c += 1
            front = q.pop(0)
            visited.add(front)
            # print(f"front.val: {front.val}")
            # if front.left:
            #     print(f"front.left: {front.left.val}")
            # if front.right:
            #     print(f"front.right: {front.right.val}")
            if equalTrees(front, subRoot):
                return True

            if front.left and front.left not in visited:
                q.append(front.left)
                visited.add(front.left)
            if front.right and front.right not in visited:
                q.append(front.right)
                visited.add(front.right)
            # if c > 50:
                # print("Infinite loop ")
                # break

        return False