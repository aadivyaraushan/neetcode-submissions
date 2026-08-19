class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # when i solve this q how do i do it?
        # lets start with 2
        # from 2, 20 is too big
        # 4 is too big
        # so for each you make 
        # but that reqs itearting n^2

        # what's the O(n) way of solving this manually?
        # at each point, if it isn't > prev by one, 
        # add it to a new sequence
        
        nums.sort()

        seq = {}
        if len(nums) == 0:
            return 0

        for num in nums:
            found = False
            for seq_start, sequence in seq.items():
                val = seq_start
                if len(sequence) > 0:
                    val = sequence[-1]
                if num - val == 1:
                    found = True
                    sequence.append(num)
            
            if not found:
                seq[num] = []
        
        # print(f"post loop, seq = {seq}")

        max_len = len(seq[nums[0]])
        for seq_start, seq in seq.items():
            max_len = max(max_len, len(seq))
        return max_len + 1