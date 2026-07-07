class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, nums):
            nonlocal ans
            ans.append(path.copy())
            if len(nums) == 0:
                return            
            for i, num in enumerate(nums):
                if num not in path:
                    path.append(num)
                    backtrack(path, nums[i+1:])
                    path.pop()
            
        backtrack([], nums)
        return ans