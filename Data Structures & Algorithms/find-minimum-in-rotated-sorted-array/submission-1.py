class Solution:
    
    def is_new_min(self, nums, n_rotations, prior_min):
        return nums[n_rotations] < prior_min

    def findMin(self, nums: List[int]) -> int:
        left_n_rotations = 0
        right_n_rotations = len(nums)
        # n_rotations also represents 
        # index of min value
        prior_min = nums[0]

        while left_n_rotations < right_n_rotations:
            mid_n_rotations = (left_n_rotations + right_n_rotations) // 2
            if self.is_new_min(nums, mid_n_rotations, prior_min):
                prior_min = nums[mid_n_rotations]
                right_n_rotations = mid_n_rotations
            else:
                left_n_rotations = mid_n_rotations + 1
        
        return prior_min