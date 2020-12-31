class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return nums[0]
        
        max_thus_far = max_temp = nums[0]
        
        # loop through list
        for i in range(1, len(nums)):
            max_temp = max(nums[i], max_temp + nums[i])
            max_thus_far = max(max_temp, max_thus_far)
                
        return max_thus_far