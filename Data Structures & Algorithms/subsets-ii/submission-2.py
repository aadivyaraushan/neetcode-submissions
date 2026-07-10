class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        visited = set()
        nums.sort()

        def backtrack(start):
            nonlocal path
            nonlocal ans

            ans.append(path.copy())

            if len(nums) == len(path):
                return
            visited = set()
            for i in range(start, len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    backtrack(i+1)
                    path.pop()
        
        backtrack(0)
        return ans