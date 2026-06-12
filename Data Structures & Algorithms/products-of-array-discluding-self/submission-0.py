class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_map = {}
        prefix = 1
        print("prefix loop")
        for i in range(1, len(nums)):
            print(f"at iteration {i}")
            prefix_map[i] = nums[i-1] * prefix
            print(f"prefix_map[{i}] = {prefix_map[i]}")
            prefix = prefix_map[i]
            print(f"prefix = {prefix_map[i]}")
        
        postfix_map = {}
        postfix = 1
        print("postfix loop")
        for i in range(len(nums)-2, -1, -1):
            print(f"at iteration {i}")
            postfix_map[i] = nums[i+1] * postfix
            print(f"postfix_map[{i}] = {postfix_map[i]}")
            postfix = postfix_map[i]
            print(f"postfix = {postfix_map[i]}")

        product_map = {}
        print("product loop")
        for i in range(0, len(nums)):
            print(f"at iteration {i}")
            if i not in prefix_map:
                product_map[i] = postfix_map[i]
            elif i not in postfix_map:
                product_map[i] = prefix_map[i]
            else:
                product_map[i] = prefix_map[i] * postfix_map[i]
            print(f"product_map[{i}] = {product_map[i]}")
        
        output = []
        for key, value in product_map.items():
            output.append(value)
        return output