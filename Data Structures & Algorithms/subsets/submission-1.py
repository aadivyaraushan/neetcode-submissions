class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path):
            nonlocal ans


            path_set = set(path)
            ans_set = [set(ans_elem) for ans_elem in ans]
            
            if len(path) > len(nums) or path_set in ans_set:
                return
            ans.append(path)

            nums_min = [num for num in nums if num not in path]
            
            
            for num in nums_min:
                backtrack(path + [num])
        backtrack([])
        return ans