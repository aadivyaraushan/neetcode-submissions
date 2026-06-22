class Solution:

    def is_new_min(self, nums, mid_rotations, prior_min):
        return nums[mid_rotations] < prior_min

    def rotate_array(self, nums, n_rotations):
        if n_rotations == -1:
            return nums
        new_nums = []

        print(f"nums: {nums}, n_rotations: {n_rotations}")
        for i in range(n_rotations, len(nums)):
            new_nums.append(nums[i])
        for i in range(0, n_rotations):
            new_nums.append(nums[i])
        return new_nums

    def is_target(self, nums, mid, target):
        return nums[mid] == target

    def search(self, nums: List[int], target: int) -> int:
        
        left_n_rotations = 1
        right_n_rotations = len(nums)
        prior_min = nums[0]
        prior_min_index = -1

        # what if we had two binary search loops?
        # one to find minimum as starting point
        # one to do binary search from that min onwards
        while left_n_rotations < right_n_rotations:
            mid_n_rotations = (left_n_rotations + right_n_rotations) // 2

            if self.is_new_min(nums, mid_n_rotations, prior_min):
                prior_min = nums[mid_n_rotations]
                prior_min_index = mid_n_rotations
                right_n_rotations = mid_n_rotations
            else:
                left_n_rotations = mid_n_rotations + 1

        print(f"found rotations: {prior_min_index}")
        
        array = self.rotate_array(nums, prior_min_index)

        print(f"rotated array: {array}")
        
        left = 0
        right = len(array)

        while left <= right :
            mid = (left + right) // 2

            if mid >= len(array):
                break

            print (f"left: {left}, right: {right}, mid: {mid}")
            print (f"target: {target}, nums[mid]: {array[mid]}")

            if target > array[mid]: 
                print (f"target is greater than nums[mid] so moving right")
                left = mid + 1
            elif target < array[mid]:
                print (f"target is lower than nums[mid] so moving left")
                right = mid - 1
            elif target == array[mid]:
                if prior_min_index == -1:
                    return mid
                print(f"found mid: {mid}")
                print(f"prior min index: {prior_min_index}")
                return (mid + prior_min_index) % len(nums)
        return -1


        


