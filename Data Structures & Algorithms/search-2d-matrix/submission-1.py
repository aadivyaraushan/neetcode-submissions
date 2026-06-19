class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            mid_m = mid // n
            mid_n = mid % n
            # ^ this calculation is wrong
            print (f"mid: {mid}")
            print (f"mid_m: {mid_m}, mid_n: {mid_n}")
            print (f"btw at this iteration left = {left} and right = {right}")

            elem = matrix[mid_m][mid_n]

            if target > elem: # element is to right of target
                left = mid + 1
            elif target < elem: # element is to left of target
                right = mid - 1
            elif target == elem:
                return True
        
        return False 
            