class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # manual walkthrough
        # input: [2, 4, -3, 5]
        # my steps;
        # variables:
        # 1. min subarray product
        # 2. max subarray product
        # 3. ending index
        # search strat, iterate from start to end and keep multiplying min, max product sum w/ elem at i
        # i.e. go from 0, 1, 2, ...
        # base case: when ending index == len(nums), return 1

        # choices at any given step:
        # 1. continue current sub-array
        # 2. start new one
        
        # walkthrough with [2, 4, -3, 5]
        # max_prod at 0 = 2
        # min_prod at 0 = 4
        # i=0, max_prod = 2, min_prod = 2
        # i=1, val=4, max_prod=8, min_prod = 8
        # i=2, val=-3, max_prod=-24, max_prod=-24
        # i=3, val=5, max_prod=5, min_prod=-120
        # i=4 -> return 1

        max_prod = []
        min_prod = []
        for i in range(len(nums)):
            max_prod.append(-1)
            min_prod.append(-1)

        min_prod[0] = nums[0]
        max_prod[0] = nums[0]

        for i in range(1, len(nums)):
            max_prod[i] = max(nums[i] * max_prod[i-1], nums[i] * min_prod[i-1], nums[i])
            min_prod[i] = min(nums[i] * max_prod[i-1], nums[i]* min_prod[i-1], nums[i])

        # print(f"max_prod: {max_prod}")
        return max(max_prod)
            



