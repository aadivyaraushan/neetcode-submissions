class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_consecutive = 0

        for num in num_set:
            if (num - 1) not in num_set:
                consecutive_count = 1
                key = num
                while num + 1 in num_set:
                    consecutive_count += 1
                    num = num + 1
                if consecutive_count > max_consecutive:
                    max_consecutive = consecutive_count
        
        return max_consecutive
                

