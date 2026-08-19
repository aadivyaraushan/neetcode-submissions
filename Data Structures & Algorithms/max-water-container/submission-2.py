class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # for ex1, how would i solve it myself?
        # at any point, what decision am i making? 
        # which side to move: left or right?
        # this depends on what's the minimum
        # if l is the minimum value, move it right
        # if r is minimum value, move it right


        # ex1  
        # lets start with bars 1, 6
        # between 

        l = 0
        r = len(heights) - 1
        max_area = 0
        while l <= r:
            # print(f"heights[l]: {heights[l]}, heights[r]: {heights[r]}, l = {l} and r = {r}")
            max_area = max(max_area, min(heights[l], heights[r]) * (r - l))
            # print(f"max_area = {max_area} between {l} and {r}")

            if heights[l] < heights[r]:
                l = l +1
            else:
                r = r -1
        return max_area