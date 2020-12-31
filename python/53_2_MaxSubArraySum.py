# Kadane’s Algorithm
# O(n) runtime & O(n) space
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return nums[0]
            
        max_thus_far = -2**31
        max_temp = 0
        
        # loop through list
        for i in nums:
            max_temp += i
            
            if max_thus_far < max_temp:
                max_thus_far = max_temp
                
            if max_temp < 0:
                max_temp = 0
                
        return max_thus_far