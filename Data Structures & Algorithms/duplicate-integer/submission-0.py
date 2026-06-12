class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists_map = {}
        for num in nums:
            exists_map[num] = False
        
        for num in nums:
            if exists_map[num] == True:
                return True
            exists_map[num] = True
        return False