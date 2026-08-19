class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # example walkthrough
        # [2, 1, 5, 1, 5, 3]
        # sliding window approach
        # 1. starting with 2
        # 2. 2 < target so lets add
        # 3. 2 + 1 < target so lets add
        # 4. 2 + 1 + 5 < target so lets add
        # 5. 2 + 1 + 5 + 1 < target so lets add
        # 6. 2 + 1 + 5 + 1 + 5 >= target. so this becomes min length for now (5) and we can move l and start to minimize
        # 7. 1 + 5 + 1 + 5 >= target. this becomes new min length and we can move l again.
        # 8. 5 + 1 + 5 >= target. this becomes new min length and we can move l again.
        # 9. 1 + 5 < target now. we can now continue as normal. minimization done.
        # 10. 1 + 5 + 3 < target.
        # 11. done with entire nums array (i.e. right pointer reached end)


        # flow at any given iteration
        # if sum < target, add right -> done presumably by loop flow control
        # if sum >= target, set current to min target and start a loop where we remove l at each iteration and update the sum while the "s" value stays >= target. once that stops being true, continue with addition in accordance with loop.

        s = 0
        l = 0
        min_length = float('inf')
        for r in range(0, len(nums)):
            s += nums[r]

            if s >= target:
                while s >= target:
                    min_length = min(min_length, r - l + 1)
                    s -= nums[l]
                    l += 1 

        if min_length == float('inf'):
            min_length = 0
        return min_length
