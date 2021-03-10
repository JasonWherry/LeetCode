# runtime: O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        
        else:
            ret = []
            for i in range(len(nums)):
                if nums[i] == target:
                    ret.append(i)

            # length = 1 so duplicate item to make range
            if len(ret) == 1:
                ret.append(ret[0])
                return ret
            
            else:
                retTuple = (ret[0], ret[-1])
                return list(retTuple)
