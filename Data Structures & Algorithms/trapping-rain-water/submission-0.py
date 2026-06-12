class Solution:



    def trap(self, height: List[int]) -> int:

     


        # amount of water at a specific pos is determined using
        # okay lets say between pos 1 and 3
        # at 2 
        # height = min(height[lower pos bound], height[higher pos bound]) - height[i]
        # so here height = min(2, 3) - 0 = 2 right

        # another test, between pos 3 and 7
        # so iterate from pos 4 to pos 6
        # at pos 4: height = min(height[lower pos bound], height[higher pos bound]) - height[4] = min(3, 3) - 1 = 2
        # at pos 5: height = min(height[lower pos bound], height[higher pos bound]) - height[5] = min(3, 3) - 0 = 3
        # at pos 6: similarly to 4, 2
        # total = 7
        
        # okay so there ^ lower pos bound = left and higher pos bound = right?
        # yes
        # if right has a higher height than left
        # then we know for sure that left is a limiting factor to the area right?
        # so we should set left to be equal to current right and right to be equal to current + 1
        # and then continue 
        # that helps us move towards a higher 
        # do we need to move in the other direction?
        # well 
        # no not really

        # and at each stage store max area

        left = 0
        right = len(height) - 1

        # print(f"starting with values: left = {left}, right = {right}, height[left] = {height[left]}, height[right] = {height[right]}")

        left_max = 0
        right_max = 0
        total_area_global = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if right_max >= left_max:
                total_area_global += left_max - height[left]
                left = left + 1
            elif left_max > right_max:
                total_area_global += right_max - height[right]
                right = right - 1
        return total_area_global

            
        # stopping condition: if all elements within range have height lower than
        # the min height of boundaries then it makes sense to calculate area 
        # otherwise reduce size and ocntinue
        # lemme fully confirm on paper before writing



       