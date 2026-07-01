# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal best
            print(f"starting: best = {best}")
            if not root.left and not root.right:
                best = max(best, root.val)
                return root.val
            elif not root.left:
                print("case where no root left")
                max_right = dfs(root.right)
                print(f"max right = {max_right}")
                output = max(root.val, root.val + max_right)
                best = max(best, output)
                return output
            elif not root.right:
                print("case where no root right")
                max_left = dfs(root.left)
                print(f"max left = {max_left}")
                output = max(root.val, root.val + max_left)
                best = max(output, best)
                return output
            print(f"root is {root.val}")
            print("starting max left")
            max_left = dfs(root.left)
            print(f"max left is {max_left}")
            print("starting max right")
            max_right = dfs(root.right)
            print(f"max right is {max_right}")
            output = max(root.val, root.val + max_left, root.val + max_right)
            best = max(output, best, root.val + max_left + max_right)
            return output
        best = root.val
        dfs(root)
        return best