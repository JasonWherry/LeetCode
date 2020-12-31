# Implement a method to 
#
# input = [-2,1,-3,4,-1,2,1,-5,4] -> output = 6
#
# input constraints:    len(input) >= 1
#
# run time O( N log(N) )
###############################################################################
import sys 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        max_sum = self.maxSubArraySum(nums, 0, len(nums) - 1)
        return max_sum
    
    
    # Find the maximum possible sum in 
    # nums[] such that nums[mid] is part of the Max Sum
    def maxMidSum(self, nums, left, mid, right) -> int:
        
        l_sum = r_sum = -2**31
        temp = 0 # tracking temporary sum
        # divide array into halves
        for i in range(mid, left-1, -1):
            temp += nums[i]
            
            if temp > l_sum:
                l_sum = temp
        
        temp = 0
        for i in range(mid+1, right+1, 1):
            temp += nums[i]
            
            if temp > r_sum:
                r_sum = temp
        
        l_r_sum = l_sum + r_sum
        
        return max( l_r_sum, l_sum, r_sum )
    
        
    def maxSubArraySum(self, nums, left, right) -> int:
        # if 1 element in nums
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2 # floor division
        
        return max(self.maxSubArraySum(nums, left, mid),
                   self.maxSubArraySum(nums, mid+1, right),
                   self.maxMidSum(nums, left, mid, right)
                  )