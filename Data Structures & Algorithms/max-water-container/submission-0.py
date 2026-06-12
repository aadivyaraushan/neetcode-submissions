class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        # area is min(lo, hi) * (hi - lo)
        # so bottleneck is the lower thing
        max_area = 0
        print(f"starting: left = {left} and right = {right}")
        while left < right:
            print(f"currently, heights[left] = {heights[left]} and heights[right] = {heights[right]}")
            area = min(heights[left], heights[right]) * (right - left)
            print(f"current area: {area}")

            if area > max_area:
                max_area = area
                print(f"current is greater than max area so max area is now {max_area}")
            
            if heights[left] < heights[right]:
                print(f"height[left] < height[right] so making left = {left+1}")
                # left is the minimum so its the bottleneck and should be moved
                left = left + 1
            elif heights[right] <= heights[left]:
                # right is the minimum and its the bottleneck so it should be moved
                print(f"height[left] >= height[right] so making right = {right-1}")
                right = right - 1
        return max_area