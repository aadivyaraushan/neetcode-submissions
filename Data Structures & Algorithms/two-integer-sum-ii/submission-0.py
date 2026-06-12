class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        print(f'target: {target}')

        while left < right:
            print (f'numbers[left] + numbers[right] = {numbers[left] + numbers[right]}')
            # if left + right is greater than target, move left -> left + 1 
            if numbers[left] + numbers[right] > target:
                print(f'right goes from {right} to {right - 1}')
                right = right - 1
            # if left + right is lower than target, move right -> right - 1 
            if numbers[left] + numbers[right] < target:
                print(f'left goes from {left} to {left + 1}')
                left = left + 1
            if numbers[left] + numbers[right] == target:
                break
        
        return [left+1, right+1]