class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # answer to q1
        # what option do i have at any index of nums when processing
        # the way i'm doing this mentally? 
        # 1) going num by num
        # 2) adding the num to a temporary "current_subsequence"
        # 3) iterating from (index of num)+1 onwarsd till end of nums
        # 4) counting an elem that is larger than last elem of current subseq and if its larger then adding that to subsequnce, continuing to iterate w/ new subsequnce afterwards
        # 5) and if it's not then not adding it and moving on to the next element i

        # variables tracking: index i in num, current subsequence, 

        def recurse(i, memo={}):
            max_len = 1
            # what does the base case here look like?
            # for me its 
            # when we reach edn then we know that the max subseq length from there is 0
            if i == len(nums):
                return 0
            if i in memo:
                return memo[i]

            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    # print(f"calling recurse({j}) from recurse({i})")
                    max_len = max(max_len, 1 + recurse(j))
            
            memo[i] = max_len
            return max_len
            
            
            # what woudl recurse(i) do?
            # recurse(i) returns max length of subsequences from and including nums[i] onwards

        max_l = 1
        for i in range(len(nums)):
            max_l = max(recurse(i), max_l)
        return max_l