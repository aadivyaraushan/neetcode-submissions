class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        
        def backtrack(visited):
            nonlocal path
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    path.append(nums[i])
                    visited_new = visited.copy()
                    visited_new.add(i)
                    backtrack(visited_new)
                    path.pop()
        
        backtrack(set())
        return ans