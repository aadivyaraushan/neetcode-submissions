class Solution:
    def rob(self, nums: List[int]) -> int:
        memo={}
        def recurse(arr, i):
            if i >= len(arr):
                return 0
            if i in memo:
                # print(f"in memo")
                return memo[i]
            
            memo[i] = arr[i]
            addition = 0
            for j in range(i+2, len(arr)):
                addition = max(addition, recurse(arr, j))
            memo[i] += addition
            
            # print(f"settling with {memo[i]} for recurse({i})")
            return memo[i]

        if len(nums) == 1:
            return nums[0]

        first = 0
        # print(f"first segment: {nums[0:len(nums)-1]}")
        # print(f"second segment: {nums[1:]}")
        for i in range(0, len(nums) - 1):
            # print(f"in first, calling for {i}")
            first = max(first, recurse(nums[0:len(nums)-1], i))
        memo = {}
        second = 0
        for i in range(0, len(nums)-1):
            # print(f"in second, calling for {i}")
            second = max(second, recurse(nums[1:], i))

        return max(first, second)

