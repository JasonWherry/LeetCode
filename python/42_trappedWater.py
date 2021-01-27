'''
the while loop assumes that the left side is the min of min(height[left], height[right])

Breaking down the problem:
- Swales fill with water
- the amount of water depends on the **minimum height of the swale's ends**
- swales can have staircase-like elevation, going in either direction
- and there can be multiple staircases (swales) per elevation map
- the end of a swale does not necessarily mark the beginning of the next


Breaking down the solution in O(n):
- loop through array and mark swale beginning(s) and end(s)
- iterate through each swale, calculating the water present with arithmetic

what determines the beginning and end of each swale?
change in elevation (height)

Draw out an example on paper, then psuedo code, then program it

Main Question is HOW DO I DETERMINE THE END OF A SWALE?

'''

# inputs
# [0,1,0,2,1,0,1,3,2,1,2,1]
# [2, 1, 0, 1, 3]
# [4,2,3]
class Solution:
    def trap(self, height: List[int]) -> int:
        # how is black vs blue recognized?
        # if a swale is present, water is trapped
            # swales can be found by subtracting elevation of sub-lists
        if not height or len(height) == 1:
            return 0
        
        for i in height:
            if i >= 10**5:
                return 0
        
        # find minimum of sub-lists (swells)
        
        # height = [2, 1, 0, 1, 3]
        water = 0
        left = 0
        for i in range(1, len(height)):
            print('left', left, '    height[left]', height[left])
            # if height[left] > max(height[left+1:]):
            #     left += 1
            # find right side of swale
            if height[i] >= height[left] and left != i:
                right = i
                # print('right', right)
                limit = min(height[left], height[right])
                print('limit', limit)
                trapped = 0
                
            # sub-routine to calculate trapped water
                while left < right:
                    # front = height[left]
                    # print('front', front)
                    if height[left] > limit: 
                        pass
                    else:
                        trapped += limit - height[left]
                        left += 1
                
                
            
            # update left to former 'right' position
                left = right
                print('right', right, '    height[right]', height[right])
                print('left', left)
                water += trapped
            
        return water