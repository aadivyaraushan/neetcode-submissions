class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O (n log n) algo

        nums.sort()
        # print(f"nums sorted: {nums}")
        output = []

        # steps = 0
        for start in range(len(nums)):
            # print(f"start: {start}")
            goal = -nums[start]
            # print(f"goal: {goal}")

            left = start + 1
            right = len(nums) - 1
            # print(f"left starts at: {left}")
            # if left < len(nums):
                # print(f"nums[left] = {nums[left]}")
            # print(f"right starts at: {right}")
            # if right < len(nums):
                # print(f"nums[right] = {nums[right]}")
            
            while left < right and right < len(nums):
                # print(f"in loop, currently left = {left} and nums[left] = {nums[left]}")
                # print(f"in loop, currently right = {right} and nums[right] = {nums[right]}")
                # print(f"in loop, goal = {goal}")
                # print(f"sum: {nums[left] + nums[right]}")
                if nums[left] + nums[right] > goal:
                    # print(f"we need to decrease sum")
                    # we need to decrease this sum
                    right = right - 1
                elif nums[left] + nums[right] < goal:
                    # print(f"we need to increase sum")
                    left = left + 1
                else:
                    # reached goal
                    # print(f"sum = goal")
                    if [nums[start], nums[left], nums[right]] not in output:
                        # print(f"found. appending {[nums[start], nums[left], nums[right]]} to output")
                        output.append([nums[start], nums[left], nums[right]])
                    left += 1
                    right = len(nums) - 1

                # steps += 1

                # if steps >= 100:
                #     print(f"LOOP IS INFINITE: left: {left}, right: {right}, nums[left]: {nums[left]}, nums[right]: {nums[right]}")
                #     break
            

            
        return output


