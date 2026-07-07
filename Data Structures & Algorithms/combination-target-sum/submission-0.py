class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(path, nums, s):
            nonlocal ans
            if s > target:
                return
            if s == target:
                ans.append(path.copy())
                return
            
            for i, num in enumerate(nums):
                path.append(num)
                backtrack(path, nums[i:], s + num)
                path.pop()
        
        backtrack([], sorted(nums), 0)
        return ans