# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # two layers here:
        # first: greedy / node by node. this is easy to check.
        # second and harder: recursively checking all left and right
        # possible solution? do a recursive method where you re-call this for each left and right and also 
        # actually wait if you do it greedily does that imply its true globally too? i think yes?
        # let me test that hypothesis -> nope this is false

        def dfs(node, l=None, u=None):
            if not node:
                return True
            
            # print(f"node = {node.val}, l.val = {l}, u.val = {u}")

            return l < node.val < u and dfs(node.left, l, node.val) and dfs(node.right, node.val, u)
            
        
        return dfs(root, float('-inf'), float('inf'))