class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(depth):
            if depth == len(nums):
                ans.append(nums.copy())
                return
            
            for i in range(depth, len(nums)):
                nums[i], nums[depth] = nums[depth], nums[i]
                backtrack(depth+1)
                nums[i], nums[depth] = nums[depth], nums[i]
        
        backtrack(0)
        return ans