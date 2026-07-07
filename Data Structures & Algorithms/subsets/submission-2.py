class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path):
            nonlocal ans

            # print(f"path: {path}")
            # print(f"ans: {ans}")
            
            if len(path) > len(nums) or sorted(path) in ans:
                # print(f"len path = len nums so returning, base case")
                return
            ans.append(sorted(path))

            nums_min = [num for num in nums if num not in path]
            
            
            for num in nums_min:
                backtrack(path + [num])
        backtrack([])
        return ans