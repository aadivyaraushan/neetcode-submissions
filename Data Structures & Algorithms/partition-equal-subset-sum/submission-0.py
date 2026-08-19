class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # what decisions do i make at any point in nums here?
        # 1) is num in either subset or is it not?
        # what info would i need for that? the two subsets
        # what info do i need to form the two subsets (looked at hint)
        # well here 1, 4 and 2,3 both work cuz they add to 5
        # 5 is half of total sum 10
        # so knowing that would help
        # is it true that if you can make half of sum with elems then
        # you can necessarily have a subset?
        # for ex1, making up 5 -> 1, 4 -> yes 
        # ex2 -> attempting to make up 15 
        # from 1: only subset is entire thing thats not subset
        # 2 -> no

        # how do i solve this myself?
        # for ex1
        # start with 1 (index 0)
        # iterate from index 1 onwards till end
        # check sequence 1 -> 2 -> 3 but then sum is 6 which is > 5 so drop that
        # ^ in this chain: after 1, sum remianing = 4
        # after 2, sum remaining = 2
        # and then nums[i] > sum remainign so we drop this chain and consider false
        # check sequence 1 -> 3 -> 4 but then sum si 8 which is > 5 so drop that
        # check sequence 1 -> 4 which matches so return True

        # so here the point is that youre checking OR for every possible index
        # post 1

        # and this happens recursively
        # so we're recursing on index
        # recurse(i) returns whether or not the array from index i onwards
        # contains a subset whose sum is equal to a certain 'remaining sum'

        # whats the base case? if i is greater than or eq to len(nums) ret True

        # do i need this remaining sum?

        if sum(nums) % 2 != 0:
            return False
        
        def recurse(i, remaining_sum=0):
            # what is this doing?
            # it should be returning whether or not nums contains subset that sums to remaining_sum from index i onwards
            # print(f"calling recurse({i}) with remaining sum = {remaining_sum}")

            if remaining_sum - nums[i] == 0:
                return True
            if nums[i] > remaining_sum:
                return False # obv, in this situation its impossible to get exactly the sum
            
            contains_subset = False
            for j in range(i+1, len(nums)):
                # print(f"calling recurse({j}) from recurse({i}) ")
                contains_subset = contains_subset or recurse(j, remaining_sum=remaining_sum-nums[i]) # checking if any of the elements can combine with i to form the req subset 


            # what does the base case look like for getting True?
            # lets say with 1
            # 1 -> 2 -> should become false
            # 1 -> 
            
            # print(f"settling on {contains_subset} for recurse({i})")

            return contains_subset


        return recurse(0, remaining_sum=sum(nums) // 2)
        