class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        
        i = 0 # slow-runner
        
        # j speeds through the list
        for j in range(0, len(nums)):
            # if new int, increment slow-runner pointer, overwrite latest duplicates
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1
        