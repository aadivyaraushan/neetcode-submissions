class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        c = 0
        while i < len(nums) - 1:
            print(f"c going from {c} -> {c+1}")
            c += 1

            maxj = i+1
            maxF = i+1+nums[i+1]
            for j in range(i+1, i+nums[i]+1):
                # print(f"inspecting {j}")
                if j >= len(nums):
                    return c
                F = j + nums[j]
                # print(f"F calculated to be {F}")
                if F >= maxF or F >= len(nums):
                    maxF = F
                    maxj = j

            # print(f"jumping from {i} to {maxj}")            
            i = maxj
            

        return c