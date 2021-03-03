import math

class Solution:
    def mySqrt(self, x: int) -> int:
        # input constraints         
        if x < 0 or x >= 2**31:
            return -1
        else:
            return math.floor(x**0.5)