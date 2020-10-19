import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # new array to return median
        nums3 = []
        
        # merge the arrays, sort the new array
        for i in nums1:
            nums3.append(i)
        for i in nums2:
            nums3.append(i)

        nums3.sort()
        # print('nums3 sorted', nums3)
        
        length = len(nums3)
        
        if length % 2 == 1:
            mid = math.floor(length/2)
            return nums3[mid]
        else:
            # print(length/2, (length/2)-1)
            mid = int(length/2)
            median = ( nums3[mid] + nums3[mid-1])/int(2)
            return median