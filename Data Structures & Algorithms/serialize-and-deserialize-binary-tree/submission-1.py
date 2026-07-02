# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        q = []
        q.append(root)
        while q:
            front = q.pop(0)
            if front:
                output.append(f"{front.val}")
                q.append(front.left)
                q.append(front.right)
            else:
                output.append(f"null")
            
        

        return ",".join(output)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        elem_vals = data.split(",")
        elems = []
        for elem_val in elem_vals:
            if elem_val == "null":
                elems.append(None)
            else:
                elems.append(TreeNode(val=elem_val))
        q = [] # queue of parent nodes to add sub nodes oto
        q.append(elems[0])
        root = elems[0]
        i = 1
        while q:
            top = q.pop(0)
            
            if not top:
                continue
            # print(f"top chosen: {top.val}")

            if i < len(elems):
                top.left = elems[i]
                top.right = elems[i+1]

            i += 2
            
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        return root
            
                



