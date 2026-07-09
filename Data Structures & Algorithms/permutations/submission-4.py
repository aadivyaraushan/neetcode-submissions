class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        visited = set()
        
        def backtrack():
            nonlocal path
            nonlocal visited
            if len(path) == len(nums):
                ans.append(path.copy())
                return
            
            for i in range(len(nums)):
                if i not in visited:
                    path.append(nums[i])
                    visited.add(i)
                    backtrack()
                    visited.remove(i)
                    path.pop()
        
        backtrack()
        return ans