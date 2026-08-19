class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:


        def is_closer(num1, num2, x):
            if abs(num1 - x) < abs(num2 - x):
                return True
            if abs(num1 - x) == abs(num2 - x) and num1 < num2:
                return True
            return False
        

        l = 0 
        r = k # exclusive upper bound
        while r < len(arr):
            # step 1: check if elem in front of current window is closer than elem at start. if it is, add that and remove one behind (i.e. r += 1, l += 1)
            # if it isn't, found closest
            # print(f"current window: {arr[l:r]}")

            # print(f"calling is_closer({arr[r]}, {arr[0]}, {x})")
            if is_closer(arr[r], arr[l], x) or arr[r] == arr[l]:
                # print(f"next is closer than previous")
                r += 1
                l += 1
            elif not is_closer(arr[r], arr[l], x):
                # closest = nums from l to r
                return arr[l:r]
        return arr[l:r]
            

        # re-run this check at end too maybe? not sure