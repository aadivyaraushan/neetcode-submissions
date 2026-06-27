# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def height_of_subtree(subtree):

            if not subtree:
                return 0

            return 1 + max(height_of_subtree(subtree.left), height_of_subtree(subtree.right))

        def sum_of_subtree_heights(subtree):
            if not subtree:
                return 0

            return height_of_subtree(subtree.left) + height_of_subtree(subtree.right)

        def dfs(root):
            nonlocal max_sum
            s = sum_of_subtree_heights(root)

            max_sum = max(s, max_sum)

            if root:
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)

        return max_sum
