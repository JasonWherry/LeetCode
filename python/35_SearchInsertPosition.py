class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # check for empty list
        if not nums:
            print('nums is Empty')
            return -1
        
        first_large = last_small = 0
        # find location for target
        for i in range(0, len(nums)):
            if nums[0] >= target:
                return 0
            if nums[i] < target:
                last_small = i
            if nums[i] >= target:
                first_large = i
                return last_small + 1
            if i == len(nums)-1:
                return len(nums)
            