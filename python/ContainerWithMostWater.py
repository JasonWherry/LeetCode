'''
height is a list
ex. input   [1,8,6,2,5,4,8,3,7]     output  49
            []                              0
            [4]                             0
'''
def maxArea(height) -> int:
    first = 0
    last = len(height) - 1
    area = 0
    
    while first < last:
        area = max(area, min(height[first], height[last]) * (last - first) )
        
        if height[first] < height[last]:
            # increment front iterator
            first += 1
        else:
            # increment back iterator
            last -= 1
            
    return area