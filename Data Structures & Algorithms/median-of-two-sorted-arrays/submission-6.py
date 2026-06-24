class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        right = len(nums1)
        
        if not nums1:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2 - 1] + nums2[(len(nums2) // 2)]) / 2
            else:
                return nums2[len(nums2) // 2]
        if not nums2:
            if len(nums1) % 2 == 0:
                return (nums1[len(nums1) // 2 - 1] + nums1[(len(nums1) // 2)]) / 2
            else:
                return nums1[len(nums1) // 2]

        count = 1

        while left <= right:
            mid = (left + right) // 2
            # print(f"mid computed to be: {mid}")

            count += 1

            if count >= 50:
                # print("INFINITE LOOP EXIT")
                break
            
            nums1_left = None
            nums1_right = None
            nums2_left = None
            nums2_right = None

            if mid < len(nums1):
                nums1_right = nums1[mid]
                # print(f"nums1_right: {nums1_right}")
            if mid - 1 >= 0:
                nums1_left = nums1[mid - 1]
                # print(f"nums1_left: {nums1_left}")
            
            j = len(nums1 + nums2) // 2 - mid
            # print (f"j (# of elems from nums2): {j}")

            if j < len(nums2):
                nums2_right = nums2[j]
                # print(f"nums2_right: {nums2_right}")
            if j - 1 >= 0:
                nums2_left = nums2[j-1]
                # print(f"nums2_left: {nums2_left}")

            if nums1_left and nums2_right and nums1_left > nums2_right:
                right = mid - 1
                continue
            elif nums2_left and nums1_right and nums2_left > nums1_right:
                # print(f"modifying right")
                left = mid + 1
                # print(f"now: left = {left} and right = {right}")
                continue
            else:
                # should be exit condition since only two fialure conditions
                # are false

                if (len(nums1) + len(nums2)) % 2 == 0:
                    if nums1_right and nums2_left:
                        return (nums1_right + nums2_left) / 2
                    else:
                        return (nums1_left + nums2_right) / 2
                else:
                    return min(nums1_right, nums2_right)