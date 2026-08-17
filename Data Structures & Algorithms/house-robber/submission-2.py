class Solution:
    def rob(self, nums: List[int]) -> int:
        def recurse(i, memo={}):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = nums[i]
            addition = 0
            for j in range(i+2, len(nums), 1):
                # print(f"from recurse({i}), calling recurse({j})")
                addition = max(addition, recurse(j))
            memo[i] += addition
            # print(f"in call recurse({i}), cost = {memo[i]} ")
            return memo[i]
        
        return max(recurse(0), recurse(1))