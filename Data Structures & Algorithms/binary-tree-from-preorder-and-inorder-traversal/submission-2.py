# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # print("INPUT VALUES")
        # print(f"preorder: {preorder}")
        # print(f"inorder: {inorder}")
        if preorder == inorder and inorder == []:
            return None
        if preorder == []:
            return TreeNode(val=inorder[0])
        if len(preorder) == 1 and preorder == inorder:
            return TreeNode(val=preorder[0])
        
        
        elem = preorder[0]
        inorder_i = inorder.index(elem)
        inorder_left = inorder[0:inorder_i]
        inorder_right = inorder[inorder_i+1:]
        preorder_left = preorder[1:len(inorder_left)+1]
        preorder_right = preorder[1+ len(inorder_left):]
        # print("COMPUTED VALS")
        # print(f"inorder_left = {inorder_left}")
        # print(f"inorder_right = {inorder_right}")
        # print(f"preorder_left = {preorder_left}")
        # print(f"preorder right = {preorder_right}")
        return TreeNode(val=elem, left=self.buildTree(preorder_left, inorder_left), right=self.buildTree(preorder_right, inorder_right))
        