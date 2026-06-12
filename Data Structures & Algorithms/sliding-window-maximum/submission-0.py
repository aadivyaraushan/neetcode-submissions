class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            last_start = len(nums) - k + 1 
            output = []

            for start in range(last_start):
                output.append(max(nums[start:start+k]))
            
            return output