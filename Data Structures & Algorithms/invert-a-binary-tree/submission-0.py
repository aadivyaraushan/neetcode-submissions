# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        if not root.left and not root.right:
            return TreeNode(val=root.val)
        else:
            # print(f"making treenode w root = {root.val}, left = {root.right.val} and right = {root.left.val}")
            return TreeNode(val=root.val, left=self.invertTree(root.right), right=self.invertTree(root.left))
        