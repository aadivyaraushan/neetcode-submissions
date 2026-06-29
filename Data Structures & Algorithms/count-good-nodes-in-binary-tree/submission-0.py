# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        p_map = {}

        q = []
        visited = set()

        q.append(root)
        c = 0

        while q:
            front = q.pop(0)

            if front.left not in visited and front.left:
                visited.add(front.left)
                q.append(front.left)
                p_map[front.left] = front
            if front.right not in visited and front.right:
                visited.add(front.right)
                q.append(front.right)
                p_map[front.right] = front
        
        # print("ENIRE MAP")
        # for key, value in p_map.items():
            # print(f"{key.val}: {value.val}")

        for key, value in p_map.items():
            # key represent child node
            # value represents parent node
            # print(f"currently inspecting {key.val}: {value.val}")
            # way to figure this out: pick each key and keep looping with using values as keys
            # till the value is equal to the parent
            # and that gives you the path
            # then ensure that the value of the node is greater than the max of that path's values

            path_values = []

            curr = key
            while True:
                # print(f"inspecting {curr.val}")
                path_values.append(curr.val)
                if curr in p_map:
                    curr = p_map[curr]
                else:
                    break
            # print(f"found path values: {path_values}, key.val = {key.val}")
            if key.val >= max(path_values):
                # print(f"{key.val} satisifes criteria ")
                c += 1

        return c + 1 