class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []
        visited = set()
        nums.sort()

        def backtrack(start):
            nonlocal path
            nonlocal ans

            # print(f"now after appending, path = {path} and we're adding that to ans")
            ans.append(path.copy())

            if len(nums) == len(path):
                return
            visited = set()
            for i in range(start, len(nums)):
                # print(f"from index {i} of {nums} onwards, visited = {visited}")
                # print(f"also, at this point, path = {path}")
                if nums[i] not in visited:
                    # print(f"appending {nums[i]}")
                    path.append(nums[i])
                    visited.add(nums[i])
                    # print(f"now visited = {visited}")
                    backtrack(i+1)
                    path.pop()
        
        backtrack(0)
        return ans