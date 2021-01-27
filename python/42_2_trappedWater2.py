class Solution:
    def trap(self, height: List[int]) -> int:
        # edge case, height is empty
        if not height: 
            return 0
        
        water = level = left = 0
        right = len(height) - 1
        
        while left < right:
            temp = ''
            # find lower side of 'swale' & iterate from that side
            if height[left] < height[right]:
                lower = height[left]
                left += 1
                temp = 'left'
                
            else:
                lower = height[right]
                right -= 1
                temp = 'right'
            
            level = max(level, lower)
            print('level', level, '   lower', lower, '   water-added', level-lower, '   temp', temp)
            
            # calculate trapped water
            water += level - lower
        
        return water