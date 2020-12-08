class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(nlogn)
        ret = set()
        
        for k in range(0, len(nums) - 2):
            target = -nums[k]
            i, j = k + 1, len(nums) - 1
            
            while i < j:
                sum_two = nums[i] + nums[j]
                
                if sum_two < target:
                    i += 1
                    
                elif sum_two > target:
                    j -= 1
                    
                else:
                    ret.add( (nums[k], nums[i], nums[j]) )
                    i += 1
                    j -= 1
                    
        return ret