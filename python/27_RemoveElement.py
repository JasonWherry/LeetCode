class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        LocList = []
        # find all locations where val appears in List
        for i in range(0, len(nums) ):
            # store them in LocList
            if nums[i] == val:
                LocList.append(i)
                
        # sort LocList backwords
        LocList.sort(reverse=True)
        for i in LocList:
            del nums[i]
        
        return len(nums)