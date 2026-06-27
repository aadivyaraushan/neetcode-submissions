# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def heightOfSubtree(subtree):
            if not subtree:
                return 0
            return 1 + max(heightOfSubtree(subtree.left), heightOfSubtree(subtree.right))
        
        delta = 0

        if not root:
            return True

        if not root.left:
            delta = heightOfSubtree(root.right)
        elif not root.right:
            delta = heightOfSubtree(root.left)
        elif not root.left and not root.right:
            delta = 0
        else:

            delta = abs(heightOfSubtree(root.left) - heightOfSubtree(root.right))

        return delta <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)