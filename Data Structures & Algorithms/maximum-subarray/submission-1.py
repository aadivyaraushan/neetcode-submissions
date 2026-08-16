class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        max_s = s

        for num in nums[1:]:
            # print(f"at {num}")
            s = max(s+num, num)
            max_s = max(max_s, s)
            # print(f"post change, s = {s}, max_s = {max_s}")
        return max_s
