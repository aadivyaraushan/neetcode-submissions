class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                return False
            maxF = i+1 + nums[i+1]
            maxj = i+1
            for j in range(i+1, i+nums[i]+1):
                if j >= len(nums):
                    return True
                F = j + nums[j]
                if F >= maxF:
                    maxF = F
                    maxj = j
            print(f"jumping from {i} to {maxj}")
            i = maxj
        

        # print(f"i: {i}, len(nums) - 1: {len(nums) - 1}")
        return i >= len(nums) -1 