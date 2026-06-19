class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # print (f"mid: {mid}") 
            # print (f"left: {left}, right: {right}")
            # print (f"nums[mid]: {nums[mid]}")

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        
        return -1