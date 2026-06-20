

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        awaiting_right_boundary_indices = []
        max_area = 0

        for index, height in enumerate(heights):
            while awaiting_right_boundary_indices and heights[awaiting_right_boundary_indices[-1]] > height:
                exclusive_right_boundary = index
                region_height = heights[awaiting_right_boundary_indices.pop()]
                left_boundary = awaiting_right_boundary_indices[-1] if awaiting_right_boundary_indices else -1
                width = (exclusive_right_boundary - left_boundary - 1) if awaiting_right_boundary_indices else index
                max_area = max(max_area, width*region_height)
            awaiting_right_boundary_indices.append(index)
        
        # for remaining indices in the awaiting right boundary indices array
        # right boundary is end of array so len(heights)

        exclusive_right_boundary = len(heights)
        while awaiting_right_boundary_indices: 
            height = heights[awaiting_right_boundary_indices.pop()]
            left_boundary = awaiting_right_boundary_indices[-1] if awaiting_right_boundary_indices else -1
            width = exclusive_right_boundary - left_boundary - 1
            max_area = max(max_area, width*height)

        return max_area