# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we're given a BST
        # so left < root < right
        # 
        curr = root
        # print(f"curr.val = {curr.val}, curr.left.val = {curr.left.val}, curr.right.val={curr.right.val}")
        while not ((p.val <= curr.val and curr.val <= q.val) or (q.val <= curr.val and curr.val <= p.val)):
            # print(f"curr.val = {curr.val}, curr.left.val = {curr.left.val}, curr.right.val={curr.right.val}")
            if p.val <= curr.val and q.val <= curr.val:
                curr = curr.left
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right

        return curr
