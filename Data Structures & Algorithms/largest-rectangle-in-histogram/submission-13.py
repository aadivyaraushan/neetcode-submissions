class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # here for the height at any index i
        # area = ((index of closest shorter height to the right) - (index of closest shorter height to the left) - 1) * height[i]

        # need to find arrays of first, second
        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)

        stack = []
        # monotonic increasing stack
        # at any given time if you find a height smaller than top of stack then keep popping from stack till thats not true
        for i in range(len(heights)):
            height = heights[i]

            while stack and heights[stack[-1]] >= height:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        # monotonic increasing stack now
        # at any given time if you find a height smaller than top of stack then keep popping til lthat's not true

        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]

            while stack and heights[stack[-1]] >= height:
                stack.pop()
            right[i] = stack[-1] if stack else len(heights)
            stack.append(i)

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, ((right[i] - left[i] - 1) * heights[i]))
        return max_area
