class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                # print(f"frrom {i}, to {j}, minimum: {min_height}")
                width = j - i + 1
                # print(f"from index {i} to index {j}, adding {min_height*width} to areas")
                max_area = max(max_area, min_height*width)
        
        return max_area