import math
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibn = math.pow(((1+sqrt5)/2), n+1) - math.pow(((1-sqrt5)/2), n+1)
        
        return int(fibn/sqrt5)