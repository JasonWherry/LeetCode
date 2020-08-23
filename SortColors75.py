"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Return nums

SOLUTION: separate 0s and 2s from the list. 0s go to the front, 2s go to the back, and the 1s are left in the middle.
"""

def sortColors(nums):
    if not isinstance(nums, (list)):
        paramType = type(nums)
        print("parameter is of type {} and needs to be of type {}".format(paramType, type([0,0])))
        return -1

    if len(nums) == 0 or len(nums) == 1:
        return nums
    
    start = 0
    end = len(nums) - 1
    curr = 0
    
    while curr <= end:
        if nums[curr] == 0:
            nums[curr] = nums[start]    # store nums[start] at nums[curr]
            nums[start] = 0             # overwrite nums[start] with a 0
            start += 1                  # start increments
            curr += 1                   # current increments
        elif nums[curr] == 2:
            nums[curr] = nums[end]      # store nums[end] at nums[curr]
            nums[end] = 2               # overwrite nums[end] with a 2
            end -= 1                    # end decrements
        else:
            curr += 1                   # 1 was found, so increment current
    
    return nums

assert(sortColors([0,2,2,2,0,2,1,1]) == [0,0,1,1,2,2,2,2]) # positive testing

assert(sortColors([2,1,2]) == [1,2,2]) # positive testing

print("input = [0,2,2,2,0,2,1,1]", " ->  output =", sortColors([0,2,2,2,0,2,1,1])) # functional testing

sortColors(3) # negative testing