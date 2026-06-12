class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):
            print(f"in this iter: i = {i}")
            print(f"in this iter: num = {num}")
            diff = target - num
            print(f"in this iter, diff = {diff}")

            if diff in index_map:
                return sorted([i, index_map[diff]])
            
            index_map[num] = i
            print(f"index_map[{num}] = {i}")